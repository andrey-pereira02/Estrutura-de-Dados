class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = Node(data, self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            return IndexError("Stack Underflow")
        temp = self.head.data
        self.head = self.head.proximo
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError("Stack is Empty")
        return self.head.valor

    def isEmpty(self):
        if self.head is None:
            return True
        return False
