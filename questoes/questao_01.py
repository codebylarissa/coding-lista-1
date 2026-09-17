def ler_inteiro():
  while(True):
    try:
      return int(input("Digite um número: "))
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")


a = ler_inteiro()
b = ler_inteiro()

if (a == 0 or b == 0):
  print("Não são múltiplos")
elif (a % b == 0 or b % a == 0):
  print("São múltiplos")
else:
  print("Não são múltiplos")