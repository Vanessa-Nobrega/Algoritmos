ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

qtd_anos = ano_atual - ano_nascimento
meses =  qtd_anos * 12
semanas = qtd_anos * 52
dias = qtd_anos * 365

print('Você tem', qtd_anos, 'anos! ')
print('Corresponde a', meses, 'meses! ')
print('corresponde a', semanas, 'semanas')
print('corresponde a', dias, 'dias ')