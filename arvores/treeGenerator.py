from arvoreBinaria import *
import random


def treeGenerator(root, qtn):
    if root is None:
        return False

    lado = 0
    lado2 = 0

    if qtn % 2 == 0:
        lado = qtn // 2
        lado2 = qtn - lado
    else:
        lado = (qtn//2) + 1
        lado2 = qtn - lado

    temp = root

    for i in range(lado):
        node = Node(random.randint(1, 10))
        sort = random.choice(["L", "R"])

        if sort == "L":
            temp.left = node
        else:
            temp.right = node

        temp = node

    temp = root

    for i in range(lado2):
        node = Node(random.randint(1, 10))
        sort = random.choice(["L", "R"])

        if sort == "L":
            temp.left = node
        else:
            temp.right = node

        temp = node

    return root


"""
Ta meio certo, mas ela não vai sair balanceada
"""
