from Listas.lista_encadeada import *


class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    def EnQueue(self, data):
        if self.isFull():
            raise OverflowError("Fila cheia !")
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data

    def DeQueue(self):
        if self.isEmpty():
            raise IndexError("Fila Vazia !")
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return data


class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def EnQueue(self, data):
        newNode = Node(data)
        if self.rear:
            self.rear.proximo = newNode
        self.rear = newNode
        if self.front is None:
            self.front = newNode

    def DeQueue(self):
        if self.isEmpty():
            raise IndexError("Fila Vazia !")
        data = self.front.data
        self.front = self.front.proximo
        if self.front is None:
            self.rear = None
        return data
