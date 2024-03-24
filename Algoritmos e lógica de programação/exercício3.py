lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))

if lado1+lado2 > lado3 or lado1+lado3 > lado2 or lado2+lado3 > lado1:
    ehTriangulo = True
else:
    ehTriangulo = False

if (ehTriangulo):
    print("Os lados formam um triângulo")
    if lado1 == lado2 == lado3:
        print("Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é um triângulo")