from filas import *
from Pilhas.pilhas_arraySimples import *


def dividindoFila(fila: QueueArray):
    if fila.isEmpty():
        return False

    count = 1
    current = fila.front

    while current != fila.rear:
        current = (current + 1) % fila.capacity
        count += 1

    tam = count // 2

    fila1 = QueueArray()

    for i in range(tam):
        fila1.EnQueue(fila.DeQueue())

    pilhaAux = Stack()
    for j in range(tam):
        pilhaAux.push(fila1.EnQueue())

    for k in range(tam):
        fila1.EnQueue(pilhaAux.pop())

    fila2 = QueueArray()
    tam = 0

    while not (fila.isEmpty()):
        fila2.EnQueue(fila.DeQueue())
        tam2 += 1

    for o in range(tam2):
        pilhaAux.push(fila2.DeQueue())

    for t in range(tam2):
        fila2.EnQueue(pilhaAux.pop())

    return fila1, fila2
