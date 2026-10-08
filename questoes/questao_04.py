def ler_inteiro(mensagem):
  while(True):
    try:
      return int(input(mensagem))
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")

n = ler_inteiro("Digite um número: ")

for i in range (1, 4 * n + 1, 4):
  print(f"{i} {i + 1} {i + 2} PUM")