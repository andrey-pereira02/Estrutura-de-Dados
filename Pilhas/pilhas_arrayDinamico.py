class Stack:
    def __init__(self, Capacity=1):
        self.Capacity = Capacity
        self.top = -1
        # Criação de um array para armazenar os itens da pilham por isso o [None]
        self.A = [None] * Capacity

    def reasize(self, dir):
        if dir == 1:
            self.Capacity *= 2
        else:
            self.Capacity //= 2
        newArray = [None] * self.Capacity
        for i in range(0, self.top + 1):
            newArray[i] = self.A[i]
        self.A = newArray

    def push(self, data):
        if self.Capacity == self.top + 1:
            self.reasize
        self.top += 1
        self.A[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        temp = self.A[self.top]
        self.top -= 1
        if self.top < self.Capacity // 2:
            self.reasize(0)
        return temp
