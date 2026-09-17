from lista_encadeada import *


def enlace_listas(lista1: LinkedList, lista2: LinkedList):
    count = 0
    current1 = lista1.head
    current2 = lista2.head

    while current1 != None:
        count += 1
        current1 = current1.proximo

    tamanho1 = count

    while current2 != None:
        count += 1
        current2 = current2.proximo

    tamanho2 = count - tamanho1

    lista3 = LinkedList()

    current1 = lista1.head
    current2 = lista2.head

    for i in range(tamanho1):
        if lista3.head is None:
            lista3.insere_valor_inicio(current1.valor)
            current1 = current1.proximo
        else:
            lista3.insere_valor_fim(current1.valor)
            current1 = current1.proximo

    for k in range(tamanho2):
        lista3.insere_valor_fim(current2.valor)
        current2 = current2.proximo
