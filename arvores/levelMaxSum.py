from Filas.filas import *


def levelMaxSum(root):
    if not root:
        return
    fila = QueueArray()
    fila.EnQueue(root)
    result = []

    while not fila.isEmpty():
        count = fila.length
        temp = 0

        for i in range(count):
            n = fila.DeQueue()
            temp += n.data

            if n.left:
                fila.EnQueue(n.left)
            if n.right:
                fila.EnQueue(n.right)

        result.append(temp)

    return max(result), (result.index(max(result)) + 1)
