class Stack:
    def __init__(self, Capacity=1):
        self.Capacity = Capacity
        self.top = -1
        # Criação de um array para armazenar os itens da pilham por isso o [None]
        self.A = [None] * Capacity
