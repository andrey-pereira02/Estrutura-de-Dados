from pilhas_arraySimples import *


class PilhaVetor:
    def __init__(self, Capacity=1):
        self.top = 0
        self.Capacity = Capacity
        self.A = [None] * Capacity

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, valor):
        if self.isEmpty():
            self.top += 1
            self.A[self.top] = valor
        else:
            self.top += 1
            self.A[self.top] = valor
            self.A[0] = self.top
