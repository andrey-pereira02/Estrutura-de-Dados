class DuasPilhas:
    def __init__(self, N):
        self.A = [None] * N
        self.N = N
        self.t1 = -1
        self.t2 = N

    def push(self, pilha, valor):
        if self.isFull():
            print("Erro: pilhas cheias.")
            return

        if pilha == 1:
            self.t1 += 1
            self.A[self.t1] = valor
        elif pilha == 2:
            self.t2 -= 1
            self.A[self.t2] = valor

    def pop(self, pilha):
        if self.isEmpty(pilha):
            print("Erro: pilha vazia.")
            return None

        if pilha == 1:
            valor = self.A[self.t1]
            self.t1 -= 1
            return valor

        elif pilha == 2:
            valor = self.A[self.t2]
            self.t2 += 1
            return valor

    def peek(self, pilha):
        if self.isEmpty(pilha):
            print("Erro: pilha vazia.")
            return None

        if pilha == 1:
            return self.A[self.t1]

        elif pilha == 2:
            return self.A[self.t2]

    def len(self, pilha):
        if pilha == 1:
            return self.t1 + 1
        elif pilha == 2:
            return self.N - self.t2

    def isEmpty(self, pilha):
        if pilha == 1:
            return self.t1 == -1
        elif pilha == 2:
            return self.t2 == self.N

    def isFull(self):
        return self.t1 + 1 == self.t2

    def empty(self):
        self.t1 = -1
        self.t2 = self.N
