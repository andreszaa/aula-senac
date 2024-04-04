import math

raio = 0

def c_a():
    raio = float(input("Digite o raio do círculo: "))
    area = 3.14*(raio*raio)
    print(f"Se o raio é:{raio:.2f}. A área é: {area:.2f}")

def c_p():
    raio = float(input("Digite o raio do círculo: "))
    perimetro = 2*3.14*raio
    print(f"Se o raio é:{raio:.2f}. O perimetro é: {perimetro:.2f}")

def menu():
    while True:
        print("\n1. Área do circulo")
        print("2. Perimetro do circulo")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            c_a()
        elif escolha == '2':
            c_p()
        elif escolha == '3':
            print("Até logo")
            return
        else: 
            print("Opção Inválida")

menu()
