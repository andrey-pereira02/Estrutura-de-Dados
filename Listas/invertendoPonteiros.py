from lista_encadeada import *


def invertP(lista: LinkedList):
    invertido = None
    atual = lista.head

    while atual != None:
        save = atual.proximo
        atual.proximo = invertido
        invertido = atual
        atual = save

    lista.head = invertido
    return lista
