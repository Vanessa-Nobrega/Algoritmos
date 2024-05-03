salario = float(input('Digite seu salário atual: '))
aumento = float(input('Digite o percentual de aumento: '))

valor_aumento = salario * (aumento / 100)
novo_salario = salario + valor_aumento
print(f"Salário atual: R$ {salario:8.2f}")
print(f"aumento......: R$ {valor_aumento:8.2f}")
print("------------------------------")
print(f"Novo salário.: R$ {novo_salario:8.2f}")
