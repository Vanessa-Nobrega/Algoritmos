def ex01(total_cabecas, total_pes):
    pato = 0
    coelho = 0

    pato = (total_pes - total_cabecas * 2)/2
    coelho = (total_cabecas - pato)
    return pato, coelho

total_cabecas = int(input("Digite o número de cabeças: "))
total_pes = total_cabecas * 3 + 3
resultado = ex01(total_cabecas, total_pes)

print(f"Total de coelhos: {resultado[1]}\nTotal de patos: {resultado[0]}")
