def ler_inteiro(mensagem):
  while(True):
    try:
      valor = int(input(mensagem))
      if (valor >= 1 and valor <= 46):
        return valor
      print("ERRO: O número deve estar entre 1 e 46")
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")

n = ler_inteiro("Digite um número: ")

anterior = 0
proximo = 1

#Caso n = 1
if n == 1:
  print(anterior)
else:
  print(f"{anterior} {proximo}", end=" ") #Imprime os dois primeiros termos se n > 2

for i in range(n - 2): # -2 para excluir os dois primeiros termos que já foram impressos
  soma = anterior + proximo
  print(f"{soma}", end=" ")

  anterior = proximo
  proximo = soma