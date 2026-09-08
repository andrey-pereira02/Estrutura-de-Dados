class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insere_valor_inicio(self, valor):
        novo = Node(valor)

        novo.proximo = self.head
        self.head = novo
        self.length += 1

    def insere_valor_fim(self, valor):
        pass

    def insere_valor_meio(self, pos, valor):  # pos é a posição
        if pos > self.length or pos < 0:
            return None
        if pos == 0:
            self.insere_valor_inicio(valor)
        if pos > self.length:
            self.insere_valor_fim(valor)
        else:
            novo = Node(valor)
            current = self.head
            count = 1
            while count < pos:
                current = current.proximo
                count += 1
            novo.proximo = current.proximo
            current.proximo = novo
            self.length += 1

    def remove_inicio(self):
        if self.length != 0:
            self.head = self.head.proximo
            self.length -= 1

    def remove_meio(self, pos):
        if pos > self.length or pos < 0:
            return None

        currentNode = self.head
        previusNode = self.head
        count = 0
        while currentNode.proximo is not None and count < pos:
            if count == pos:
                previusNode.proximo = currentNode.proximo
                self.length -= 1
            previusNode = currentNode
            currentNode = currentNode.proximo
            count += 1

    def imprimir(self):
        atual = self.head

        while atual:
            print(atual.valor, end="->")
            atual = atual.proximo

        print("None")

    def media(self):
        atual = self.head
        soma = 0
        qntNo = 0

        while atual:
            soma += atual.valor
            qntNo += 1
            atual = atual.proximo

        media = soma / qntNo
        print("A media de valores dessa lista encadeada é %d" % (media))

    def maiorValor(self):
        atual = self.head
        maior = self.head.valor

        while atual:

            if maior < atual.valor:
                maior = atual.valor

            atual = atual.proximo

        print("O maior valor dessa lista encadeada é %d" % (maior))


n = LinkedList()
n.insere_valor_inicio(10)
n.insere_valor_inicio(20)
n.insere_valor_inicio(30)

n.imprimir()
n.media()
n.maiorValor()
