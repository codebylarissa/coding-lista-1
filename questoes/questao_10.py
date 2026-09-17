def ler_mensagem(mensagem, min_total, max_total):
  while(True):
      texto = input(mensagem).upper()
      if (len(texto) >= min_total and len(texto) <= max_total):
        return texto
      print(f"ERRO: A mensagem precisa ter entre {min_total} e {max_total} caracteres")
    

mensagem = ler_mensagem("Digite a mensagem: ", 1, 104)
crib = ler_mensagem("Digite o crib: ", 1, len(mensagem))

posicao = 0

#Testa cada posição da mensagem onde o crib cabe por inteiro
for i in range(len(mensagem) - len(crib) + 1): 
  #len(mensagem) - len(crib) + 1 = Se mensagem possuir tamanho 12 e o crib tamnho 6 o calculo será: 12-6+1 = 7 (0 a 6 posições)
  valida = True
  for j in range(len(crib)):
    if (mensagem[i + j] == crib[j]):#i+j serve para o crib deslizar entre as letras da mensagem
      valida = False 
      break

  if (valida):
    posicao += 1
  
print(posicao)