class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class NodeDoubly:
    def __init__(self, valor, proximo, previo):
        self.valor = valor
        self.proximo = proximo
        self.previo = previo


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

    def remove_fim(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.length = 0
            return

        currentNode = self.head
        previousNode = None

        while currentNode.proximo is not None:
            previousNode = currentNode
            currentNode = currentNode.proximo
        previousNode.proximo = None
        self.length -= 1

    def imprimir(self):
        atual = self.head

        while atual:
            print(atual.valor, end="->")
            atual = atual.proximo

        print("None")

    def imprimir_inverso(self):
        atual = self.head
        lista_nos = []

        while atual:
            lista_nos.append(atual)
            atual = atual.proximo

        while lista_nos:
            atual = lista_nos.pop()
            print(atual.valor, end="->")

        print("None")

    # Imprimindo de tras para frente com recursão, lembre-se que a recursão ela gera uma pilha de recusões e dps imprime do final para o começo
    def imprimir_end(self):
        def imprimir(atual):
            if atual is None:
                return

            imprimir(atual.proximo)
            print(atual.valor, end="->")

        imprimir(self.head)
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

# Classe de lista duplamente encadeada


class DoublyLL:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.length = 0

    def inserir_inicio(self, valor):
        newNode = NodeDoubly(valor, None, None)
        if self.head == None:
            self.head = newNode
        else:
            newNode.previo = None
            newNode.proximo = self.head
            self.head.previo = newNode
            self.head = newNode
        self.length += 1

    def inserir_fim(self, valor):
        if self.head == None:
            self.head = NodeDoubly(valor)
        else:
            current = self.head
            while current.proximo != None:
                current = current.proximo
            newNode = NodeDoubly(valor)
            newNode.previo = current
            newNode.proximo = None
            current.proximo = newNode
        self.length += 1

    def inserir_meio(self, pos, valor):
        if pos < 0 or pos > self.length:
            raise IndexError("Erro: Posição inserida fora dos limites")

        if pos == 0:
            self.inserir_inicio(valor)
            return

        if pos == self.length:
            self.inserir_fim(valor)
            return

        newNode = NodeDoubly(valor)

        current = self.head
        for i in range(pos):
            current = current.proximo
        previous = current.prev
        newNode.proximo = current
        newNode.previo = previous
        previous.proximo = newNode
        current.previo = newNode
        self.length += 1

    def remover_inicio(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.proximo
            self.head.prev = None
        self.length -= 1

    def remover_fim(self):
        if self.head == None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.proximo != None:
                current = current.proximo
            previous = current.previo
            previous.proximo = None
            self.tail = previous
            #         OU
            # self.tail = self.tail.previo
            # self.tail.proximo = None
            # Desse jeito a complexidade é de O(1), pois ele não precisa percorrer toda a lista, ele acessa direto o ultimo e tira as referencias
        self.length -= 1

    def remove_meio(self, pos):
        if pos < 0 or pos > self.length:
            return
        if pos == 0:
            return self.remover_inicio(self)
        if pos == self.length:
            return self.remover_fim(self)
        else:
            current = self.head
            count = 0
            while count < pos:
                current = current.proximo
                count += 1
            previous = current.previo
            after = current.proximo

            previous.proximo = after
            after.previo = previous

        self.length -= 1

    def imprimir_doublyLL(self):
        current = self.head

        while current.proximo != None:
            print(current.valor, end="->")
            current = current.proximo

    def imprimir_inverso_doublyLL(self):
        current = self.head
        lista = []

        while current.proximo != None:
            lista.append(current.valor)
            current = current.proximo

        while lista:
            atual = lista.pop()
            print(atual.valor, end="->")

        print("None")


def detectCycle(linkedList: LinkedList):
    fast = slow = linkedList.head
    while (fast != None and slow != None):
        fast = fast.proximo
        if (fast == slow):
            return True
        if (fast == None):
            return False
        fast = fast.proximo
        if (fast == slow):
            return True
        slow = slow.proximo
    return False


n = LinkedList()
n.insere_valor_inicio(10)
n.insere_valor_inicio(20)
n.insere_valor_inicio(30)

n.imprimir()
n.media()
n.maiorValor()
n.imprimir_inverso()
n.imprimir_end()
