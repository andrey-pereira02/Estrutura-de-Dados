from Filas.filas import *
from Pilhas.pilha_vetor import *


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.father = None
        self.isLeft = None

    def setLeft(self, data):
        self.left = Node(data)
        self.isLeft = True

    def setRight(self, data):
        self.right = Node(data)
        self.isLeft = False


class BinTree:
    def __init__(self, root=None):
        self.root = root

    def preOrder(self, root):
        if root == None:
            return
        print(root.data, sep="-->", end="-->")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def preOrderIterative(self, root, result):
        if not root:
            return
        stack = Stack()
        stack = [root]
        while stack:
            n = stack.pop()
            result.append(n.data)

            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)

    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data, sep="-->", end="-->")
        self.inOrder(root.right)

    def inOrderIterative(self, root, result):
        if not root:
            return
        stack = []
        n = root
        while n or stack:
            if n:
                stack.append(n)
                n = n.left
            else:
                n = stack.pop()
                result.append(n.data)
                n = n.right

    def postOrder(self, root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, sep="-->", end="-->")

    def postOrderIterative(self, root, result):
        if not root:
            return
        stack = []
        visited = set()
        n = root
        while n or stack:
            if n:
                stack.append(n)
                n = n.left
            else:
                n = stack.pop()
                if n.right and n.right not in visited:
                    stack.append(n)
                    n = n.right
                else:
                    visited.add(n)
                    result.append(n.data)
                    n = None

    def levelOrder(self, root, result):
        if not root:
            return
        q = QueueArray()
        q.EnQueue(root)
        while not q.isEmpty():
            n = q.DeQueue()
            result.append(n.data)

            if n.left:
                q.EnQueue(n.left)
            if n.right:
                q.EnQueue(n.right)

        return result
