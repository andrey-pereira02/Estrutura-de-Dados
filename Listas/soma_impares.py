from lista_encadeada import *


def soma_impares(lista: LinkedList):
    currentNode = lista.head
    soma = 0
    while currentNode.proximo != None:
        if currentNode.valor % 2 != 0:
            soma += currentNode.valor
        currentNode = currentNode.proximo

    return soma
