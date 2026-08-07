frase = input("Digite uma frase : ")
lista = list(frase)
set = set(lista)
meu_dicionario = {}

for i in set:
    meu_dicionario[i] = lista.count(i)

print(meu_dicionario)
