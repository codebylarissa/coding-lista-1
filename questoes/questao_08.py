def ler_inteiro(mensagem, min_total, max_total):
  while(True):
    try:
      valor = int(input(mensagem))
      if (valor >= min_total and valor <= max_total):
        return valor
      print(f"ERRO: O valor precisa ser entre {min_total} e {max_total}")
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")

n = ler_inteiro("Digite a quantidade de protesto:", 1, 100)

for i in range(1,n+1):
  reclamacao = ler_inteiro("Digite a quantidade de reclamações: ", 0, 100)
  if (reclamacao == 0):
    print("Vai ter copa!")
  else:
    print("Vai ter duas!")
