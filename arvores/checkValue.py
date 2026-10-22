from Filas.filas import *


def checkValue(root, value):
    if root is None:
        return False

    if root.data == value:
        return True

    return checkValue(root.left, value) or checkValue(root.right, value)


def checkValueIterative(root, value):
    if root is None:
        return

    q = QueueArray()
    q.EnQueue(root)

    while not q.isEmpty():
        temp = q.DeQueue()

        if temp.data == value:
            return True

        if temp.left:
            q.EnQueue(temp.left)
        if temp.right:
            q.EnQueue(temp.right)

        return False
