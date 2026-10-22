from isStrictBinTree import *
from Filas.filas import *
from countDeep import *


def isFullBinTree(root):
    """Algoritmo de arvore cheia"""
    if not root:
        return False

    if not isStrictBinTree(root):
        return False

    if isStrictBinTree(root):
        count = 0
        result = []
        q = QueueArray()
        q.EnQueue(root)
        while not q.isEmpty():
            count = q.lenght
            temp = 0

            for i in range(count):
                n = q.DeQueue()
                temp += 1

                if n.left:
                    q.EnQueue(n.left)
                if n.right:
                    q.EnQueue(n.right)

            result.append(temp)

        for i in range(len(result)):
            if result[i] != 2 ** i:
                return False

        return True


def isFullBinTree2(root):
    """Algoritmo de arvore cheia"""
    if not root:
        return False

    if not isStrictBinTree(root):
        return False

    if coutDeep(root.left) == coutDeep(root.right):
        return False

    return (isFullBinTree2(root.left) and isFullBinTree2(root.right))
