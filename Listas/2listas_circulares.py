from lista_encadeada import *


def dividirListas(lista: LinkedList):
    # Conta os elementos
    count = 0
    current = lista.head

    while current != None:
        count += 1
        current = current.proximo

    # Encontra o meio
    metade = count // 2

    # Primeiro elemento da segunda lista
    current = lista.head

    for _ in range(metade - 1):
        current = current.proximo

    inicio2 = current.proximo

    # Separa as duas listas
    current.proximo = None

    # Cria as listas
    lista1 = LinkedList()
    lista2 = LinkedList()

    lista1.head = lista.head
    lista2.head = inicio2

    # Encontra o último nó da primeira lista
    ultimo1 = lista1.head
    while ultimo1.proximo != None:
        ultimo1 = ultimo1.proximo

    # Encontra o último nó da segunda lista
    ultimo2 = lista2.head
    while ultimo2.proximo != None:
        ultimo2 = ultimo2.proximo

    # Torna as listas circulares
    ultimo1.proximo = lista1.head
    ultimo2.proximo = lista2.head

    return lista1, lista2
