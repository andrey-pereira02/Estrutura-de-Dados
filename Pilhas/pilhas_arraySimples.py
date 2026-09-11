class Stack:
    def __init__(self, Capacity=1):
        self.Capacity = Capacity
        self.top = -1
        # Criação de um array para armazenar os itens da pilham por isso o [None]
        self.A = [None] * Capacity

    def push(self, valor):
        if self.Capacity == self.top + 1:
            print("Stack Overflow")
            return
        else:
            self.top += 1
            self.A[self.top] = valor

    def pop(self):
        if self.top == -1:
            print("Pilha Vazia")
            return
        temp = self.A[self.top]
        # desse jeito vc tbm zerar o valor daquela posição ao contrario de só mover o top para o elemento anterior
        self.A[self.top] = None
        self.top -= 1
        return temp

    def peek(self):
        if self.top == -1:
            return None
        else:
            temp = self.A[self.top]
            return temp

    def isEmpTy(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top + 1 == self.Capacity:
            return True
        else:
            return False
