v = 0
frase = input("Digite a frase: ")
for vogal in "AEIOUaeiou":
    v = v + frase.count(vogal)
print(f"A frase tem {v} vogal(is).")