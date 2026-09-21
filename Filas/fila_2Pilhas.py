from filas import *
from Pilhas.pilhas_arraySimples import *

s1 = Stack()
s2 = Stack()


def enQueue(data):
    s1.push(data)


def deQueue():
    while (not s1.isEmpTy()):
        s2.push(s1.pop())
    data = s2.pop()

    return data
