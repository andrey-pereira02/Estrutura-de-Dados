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

    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data, sep="-->", end="-->")
        self.inOrder(root.right)

    def postOrder(self, root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, sep="-->", end="-->")
