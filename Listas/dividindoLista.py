from lista_encadeada import *


def dividindo(lista: LinkedList):
    count = 0
    current = lista.head

    while current.proximo != None:
        count += 1
        current = current.proximo

    tam = count // 2
    current = lista.head

    for i in range(tam):
        current = current.proximo

    lista2 = LinkedList()
    current2 = current.proximo
    lista2.head = current2

    current.proximo = None

    return lista, lista2
