def ler_inteiro(mensagem):
  while(True):
    try:
      valor = int(input(mensagem))
      if (valor >= 1 and valor <= 1000):
        return valor
      print("ERRO: O número deve estar entre 1 e 1000")
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")

x = ler_inteiro("Digite um número: ")

for i in range(1, x + 1, 2): #Começa em 1 e pula de dois em dois
    print(i)