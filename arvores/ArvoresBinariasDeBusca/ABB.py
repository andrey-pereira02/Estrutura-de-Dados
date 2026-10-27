class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinSearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def print_tree(self):

        def inorder(node):
            if node is not None:
                inorder(node.left)
                print(node.key, end=" ")
                inorder(node.right)

        inorder(self.root)
        print()

    def deleteNode(self, key):
        self.root = self._deleteNode(self.root, key)

    def _deleteNode(self, root, key):

        if root is None:
            return None

        if key < root.key:
            root.left = self._deleteNode(root.left, key)
        elif key > root.key:
            root.right = self._deleteNode(root.right, key)
        else:

            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            sucessor = self.minValueNode(root.right)
            root.key = sucessor.key

            root.right = self._deleteNode(
                root.right, sucessor.key
            )

        return root
