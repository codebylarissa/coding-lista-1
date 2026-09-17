def ler_inteiro(mensagem):
  while(True):
    try:
      return int(input(mensagem))
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")

n = ler_inteiro("Digite um número: ")

num = 1 #Contador para gerar a sequência de números
for i in range(n): #Cria as linhas
  for j in range(1,4): #Roda 3 vezes já que cada linha tem 3 números
    print(num, end=" ") #Imprime 3 números na mesma linha
    num += 1 #Soma +1 para continuar a sequência
  print("PUM")
  num += 1 #Soma +1 para não contar o número que foi susbtituido por PUM