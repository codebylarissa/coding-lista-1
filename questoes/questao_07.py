def ler_inteiro(mensagem):
  while(True):
    try:
      return int(input(mensagem))
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")

n = ler_inteiro("Digite um número: ")

answer = []

#Adiciona os números interios
for i in range(1, n+1):
  answer.append(i)

#Substitui os números caso a condição do if for verdadeira
for i in range(len(answer)):
  if (answer[i] % 3 == 0 and answer[i] % 5 == 0):
    answer[i] = "FizzBuzz"
  elif (answer[i] % 3 == 0):
    answer[i] = "Fizz"
  elif (answer[i] % 5 == 0):
    answer[i] = "Buzz"

#Transforma em String
for i in range(len(answer)):
  answer[i] = str(answer[i])

#Exibe a lista em String
for i in answer:
  print(i)