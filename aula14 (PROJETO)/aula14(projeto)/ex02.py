def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def lista_primos(limite):
    maximo = limite * 2 + 5
    lista_primos = []
    for i in range(2, maximo + 1):
        if eh_primo(i):
            lista_primos.append(i)
    return lista_primos


def soma_primos(primos):
    return sum(primos)


limite = 31
primos_ate_limite = lista_primos(limite)
soma_dos_primos = soma_primos(primos_ate_limite)
print(f"Dois últimos números do RA: {limite}")
print(f"Lista de números primos até {limite * 2 + 5}: {primos_ate_limite}")
print(f"A soma dos números primos até {limite * 2 + 5} é {soma_dos_primos}.")