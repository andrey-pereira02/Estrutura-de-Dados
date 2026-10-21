from Filas.filas import *
from arvoreBinaria import *


def maiorNo(root):
    if root is None:
        return float('-inf')

    maior_esquerda = maiorNo(root.left)
    maior_direita = maiorNo(root.right)

    return max(root.valor, maior_esquerda, maior_direita)


def maiorNoInterativo(root):
    if root is None:
        return None

    fila = QueueArray()
    fila.EnQueue(root)
    maior = float('-inf')

    while not fila.isEmpty():
        atual = fila.DeQueue()

        if atual.data > maior:
            maior = atual.data

        if atual.left:
            fila.EnQueue(atual.left)

        if atual.right:
            fila.EnQueue(atual.right)

    return maior
