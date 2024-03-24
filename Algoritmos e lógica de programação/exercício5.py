num_ano = int(input("Digite um número correspondente à um ano: "))

bissexto = False
if (num_ano % 4 == 0):
    bissexto = True
    if (num_ano % 100 == 0) and (num_ano % 400 != 0):
        bissexto = False

if (bissexto):
    print('O ano é BISSEXTO')
else:
    print('O ano NÃO É BISSEXTO')