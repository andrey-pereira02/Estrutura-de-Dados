from lista_encadeada import *


def removerImpares(lista: LinkedList):
    current = lista.head
    previous = lista.head

    while current.proximo != None:
        if current.valor % 2 != 0:
            if current == lista.head:
                lista.head = lista.head.proximo
            else:
                previous.proximo = current.proximo

            current = current.proximo

        else:
            previous = current
            current = current.proximo

    return lista
