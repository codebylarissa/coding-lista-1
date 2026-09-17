def ler_inteiro(mensagem):
  while(True):
    try:
      return int(input(mensagem))
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")

a = ler_inteiro("Digite o 1° número: ")
b = ler_inteiro("Digite o 2° número: ")
c = ler_inteiro("Digite o 3° número: ")

numeros = [a, b, c] 
original = numeros.copy()

#Ordenação com Bubble Sort
n = len(numeros) #Tamanho da lista
for i in range(n - 1): #Contador das rodadas
  for j in range(n - 1 - i): #Contador das trocas
    if (numeros[j] > numeros[j + 1]): #Verifica os valores da esquerda com o da direita
      numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print("\nValores ordenados")
for i in numeros:
  print(i)

print("\nValores na ordem original")
for i in original:
  print(i)

print("\nOrdenação com método sort()")
original.sort()
print(original)