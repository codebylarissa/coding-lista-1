def menu():
  print("======= Pesquisa de Preferência =======")
  texto = '''
  1. Álcool
  2. Gasolina
  3. Diesel
  4. Sair
  Escolha uma opção: '''
  print(texto)

def ler_opcoes():
  while(True):
    menu()
    try:
      opcao = int(input())
      if(opcao >= 1 and opcao <= 4):
        return opcao
      print("ERRO: Digite uma opção entre 1 e 4")
    except ValueError:
      print("ERRO: Valor inválido! Digite apenas números inteiros")


alcool_total = 0
diesel_total = 0
gasolina_total = 0

while(True):
  opcao = ler_opcoes()

  if (opcao == 4):
    break

  match opcao:
    case 1:
      alcool_total += 1
    case 2:
      gasolina_total += 1
    case 3:
      diesel_total += 1

print("Muito Obrigado")
print("Álcool", alcool_total)
print("Gasolina", gasolina_total)
print("Diesel", diesel_total)

