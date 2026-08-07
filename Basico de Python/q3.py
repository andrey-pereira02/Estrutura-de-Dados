frase = str(input("Digite uma frase : "))
n = 1

for i in frase:
    n += 1

print(frase[-1:-n:-1])
