from math import prod

num = str(input("Digite o número do seu RA: "))
ls_num = list(num)
lista_inteiro = []
print(ls_num)
for i in ls_num:
    lista_inteiro += [int(i)]

print(f"Multiplicação = {prod(lista_inteiro)}")
print(f"Soma = {sum(lista_inteiro)}")