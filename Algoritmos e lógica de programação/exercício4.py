import math
valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
valorC = float(input("Digite o valor de C: "))
print('ax2 + bx + c = 0')

if valorA == 0:
    print("Não é uma equação de 2 grau")
else:
    delta = math.pow(valorB,2) - (4 * valorA * valorC)

    if delta < 0:
        print("A equação não tem raízes reais")
    elif delta == 0:
        print('A equação possui apenas uma raiz')
        raiz = -(valorB) / (2 * valorA)
        print('Raiz:', raiz)
    else:
        print('A equação possui duas raizes')
        raiz1 = (-(valorB) + math.sqrt(delta)) / (2 * valorA)
        raiz2 = (-(valorB) - math.sqrt(delta)) / (2 * valorA)
        print('Raiz 1:', raiz1)
        print('Raiz 2:', raiz2)
