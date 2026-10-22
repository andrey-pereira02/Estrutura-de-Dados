from Filas.filas import *


def coutDeep(root):
    if not root:
        return
    fila = QueueArray()
    fila.EnQueue(root)
    count = 1
    deep = 0

    while not fila.isEmpty():
        count = fila.length

        for i in range(count):
            n = fila.DeQueue()

            if n.left:
                fila.EnQueue(n.left)
            if n.right:
                fila.EnQueue(n.right)

        deep += 1

    return deep
