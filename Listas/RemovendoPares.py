from lista_encadeada import *


def remover_pares(lista: LinkedList):
    previousNode = lista.head
    currentNode = lista.head
    while currentNode.proximo != None:
        if currentNode.data % 2 == 0:
            previousNode.proximo = currentNode.proximo
            previousNode = currentNode
        currentNode = currentNode.proximo

    return lista
