from lista_encadeada import *
from invertendoPonteiros import *
from dividindoLista import *


def palindromo(lista: LinkedList):
    L1, L2 = dividindo(lista)
    invertP(L2)

    current1 = L1.head
    current2 = L2.head

    while current1 != None:
        if current1 .valor != current2.valor:
            return False
        current1 = current1.proximo
        current2 = current2.proximo

    return True
