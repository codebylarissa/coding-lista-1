import math

def ler_funcionarios(mensagem):
  while(True):
    try:
      f = int(input(mensagem))

      if (f > 0 and f <= 1000):
        return f
      print("ERRO: A quantidade de funcionários deve ser entre 1 e 1000")
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")

a1 = ler_funcionarios("Quantidade de funcionarios do 1° andar: ")
a2 = ler_funcionarios("Quantidade de funcionarios do 2° andar: ")
a3 = ler_funcionarios("Quantidade de funcionarios do 3° andar: ")

#Tempo total de deslocamento entre os andares
t1 = (a2 * 2) + (a3 * 4) #Máquina no 1° andar
t2 = (a1 * 2) + (a3 * 2) #Máquina no 2° andar
t3 = (a1 * 4) + (a2 * 2) #Máquina no 3° andar

print("Tempo total de deslocamento no 1° andar: ", t1)
print("Tempo total de deslocamento no 2° andar: ", t2)
print("Tempo total de deslocamento no 3° andar: ", t3)

print("O menor tempo é", min(t1, t2, t3))