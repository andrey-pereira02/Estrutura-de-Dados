from Heaps import *


class Queue:
    def __int__(self):
        self.heap = minHeap()
        self.prioridade = 0

    def enQueue(self, value):
        self.heap.add(self.prioridade, value)
        self.prioridade += 1

    def deQueue(self):
        valor = self.heap.remove()
        if self.heap.isEmpty():
            self.prioridade = 0
        return valor
