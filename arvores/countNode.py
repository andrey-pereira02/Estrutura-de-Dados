from Filas.filas import *


def countNode(root):
    if root is None:
        return 0

    return 1 + countNode(root.left) + countNode(root.right)


def countNodeIterative(root):
    if root is None:
        return False
    fila = QueueArray()
    fila.EnQueue(root)
    contador = 0

    while fila is not None:
        atual = fila.DeQueue()
        contador += 1

        if atual.left:
            fila.EnQueue(atual.left)

        if atual.right:
            fila.EnQueue(atual.right)

    return contador
