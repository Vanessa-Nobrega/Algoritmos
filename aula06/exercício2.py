valor_compra = float(input("Digite o valor da compra: "))

if valor_compra <= 1000.00:
    desconto = valor_compra - (valor_compra * 0.1)
    print("Sua compra deu:  R$", desconto)
elif valor_compra <= 5000.00:
    desconto = valor_compra - (valor_compra * 0.2)
    print("Sua compra deu:  R$", desconto)
else:
    desconto = valor_compra - (valor_compra * 0.3)
    print("Sua compra deu:  R$", desconto)