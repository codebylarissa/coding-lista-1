def ler_inteiro(mensagem):
  while(True):
    try:
      return int(input(mensagem))
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")

n = ler_inteiro("Digite um número: ")

def fizzBuzz(n):
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)


fizzBuzz(n)