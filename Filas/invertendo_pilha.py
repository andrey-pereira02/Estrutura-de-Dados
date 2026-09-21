from Pilhas.pilhas_arraySimples import *
from filas import *

# Invertendo fila com pilha


def invert(fila: QueueArray):
    pilha = Stack()

    while (not fila.isEmpty()):
        pilha.push(fila.DeQueue())

    while (not pilha.isEmpTy()):
        fila.EnQueue(pilha.pop())

# Invertendo uma pilha com fila


def invert2(pilha: Stack):
    fila = QueueArray()

    while (not pilha.isEmpty()):
        fila.EnQueue(pilha.pop())

    while (not fila.isEmpty()):
        pilha.push(fila.DeQueue())


def invertN(fila: QueueArray, n: int):
    pilha = Stack()

    for i in range(n):
        pilha.push(fila.DeQueue())

    for k in range(n):
        fila.EnQueue(pilha.pop())

    for j in range(fila.length - n):
        fila.EnQueue(fila.DeQueue())
