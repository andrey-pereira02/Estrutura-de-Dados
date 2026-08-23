class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insere_valor(self, valor):
        novo = Node(valor)

        novo.proximo = self.head
        self.head = novo

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
n.insere_valor(10)
n.insere_valor(20)
n.insere_valor(30)

n.imprimir()
n.media()
n.maiorValor()
