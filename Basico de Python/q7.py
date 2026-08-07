frase_1 = str(input("Digite uma frase: "))
lista_1 = list(frase_1)
set_1 = set(lista_1)

frase_2 = str(input("Digite uma frase : "))
lista_2 = list(frase_2)
set_2 = set(lista_2)

intersecao = set_2 & set_1
print(f"A interseção entre as duas frases é {intersecao}")
