from pilhas_arraySimples import *


class PilhaVetor:
    def __init__(self, Capacity=1):
        self.top = 0
        self.Capacity = Capacity
        self.A = [None] * Capacity
        self.A[0] = 0

    def isEmpty(self):
        if self.A[0] == 0:
            return True
        else:
            return False

    def push(self, valor):
        if self.isFull():
            return "Esta Cheia"

        self.A[0] += 1
        self.A[self.A[0]] = valor

    def pop(self):
        if self.isEmpty():
            return "Já esta vazia"

        temp = self.A[self.A[0]]
        self.A[self.A[0]] = None
        self.A[0] -= 1

        return temp

    def peek(self):
        return self.A[self.A[0]]

    def len(self):
        return self.A[0]

    def isFull(self):
        if self.A[0] == self.Capacity - 1:
            return True
        else:
            return False

    def empty(self):
        while not self.isEmpty():
            self.pop()
