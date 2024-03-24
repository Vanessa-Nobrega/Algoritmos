valor_hora = float(input("Digite o valor da hora: "))
qtd_hora = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = qtd_hora * valor_hora

if salario_bruto > 2500:
    aliquotaIR = 0.2
elif salario_bruto > 1500:
    aliquotaIR = 0.1
elif salario_bruto > 900:
    aliquotaIR = 0.05
else:
    aliquotaIR = 0

valorIR = salario_bruto * aliquotaIR

INSS = salario_bruto * 0.1
FGTS = salario_bruto * 0.11
total_descontos = valorIR + INSS
sindicato = salario_bruto * 0.03
sal_liquido = salario_bruto - total_descontos

print("Salário bruto: (", valor_hora, "*", qtd_hora, "):  R$", salario_bruto)
print('(-) IR (', aliquotaIR, '%): R$', valorIR)
print('(-) Sindicato ( 3 %): R$', sindicato)
print("INSS (10%) :  R$", INSS)
print('FGTS ( 11 %): R$', FGTS)
print('Total de Descontos: R$', total_descontos)
print('Salario Liquido: R$', sal_liquido)
