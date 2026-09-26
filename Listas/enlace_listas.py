from lista_encadeada import *


def enlace_listas(lista1: LinkedList, lista2: LinkedList):
    current1 = lista1.head
    current2 = lista2.head
    lista3 = LinkedList()

    while current1 is not None and current2 is not None:
        if current1 is not None:
            lista3.insere_valor_fim(current1.valor)
            current1 = current1.proximo

        if current2 is not None:
            lista3.insere_valor_fim(current2.valor)
            current2 = current2.proximo

    return lista3
