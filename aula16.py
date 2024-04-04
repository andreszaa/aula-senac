from random import randint

def numero_aleatorio():
  aleatorio=randint(1,100)
  palpite =0
  tentativa = 0
  while aleatorio != palpite:
    tentativa +=1
    palpite = int(input("Digite um valor (1 a 100): "))
    if aleatorio == palpite:
      print("Parabéns, o número gerado foi ", aleatorio, "Acertou em", tentativa, "Tentativas!" )
    elif aleatorio > palpite:
        print("O número sorteado é maior que ", palpite)
    elif aleatorio < palpite:
        print("O número sorteado é menor ", palpite)
    else:
      print("Tente novamente.")
numero_aleatorio()
