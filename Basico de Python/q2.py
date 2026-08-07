flag = False
lista = []

while (flag == False):
    numero = int(input(
        "Digite um numero para incrementar(Se quiser parar a execução digite 999) : "))
    if numero == 999:
        flag = True
    else:
        lista.append(numero)

print(f'A soma da lista é {sum(lista)}')
print(f'O maior número digitado é {max(lista)}')
print(f'O menor número digitado é {min(lista)}')
