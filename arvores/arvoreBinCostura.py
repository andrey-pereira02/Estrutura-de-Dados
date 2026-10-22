class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.ltag = 1
        self.rtag = 1


def threadify(root):
    prev = [None]

    def _inorder(n):
        if not n:
            return
        _inorder(n.left)
        if n.left is None:
            n.ltag = 0
            n.left = prev[0]

        if prev[0] is not None and prev[0].right is None:
            prev[0].rtag = 0
            prev[0].right = n
        prev[0] = n
        _inorder(n.right)

    _inorder(root)
    return root


def add_dummy(root):
    if not root:
        return None

    p = root
    while p.rtag == 1 and p.right:
        p = p.right
    dummy = TNode(None)
    dummy.ltag, dummy.left = 1, root
    dummy.rtag, dummy.right = 0, dummy

    p.rtag, p.right = 0, dummy
    return dummy


def inorder_successor(p):
    if p.rtag == 0:
        return p.right

    p = p.right
    while p.ltag == 1:
        p = p.left
    return p


def inorder_traversal(dummy):
    p = inorder_successor(dummy)
    while p is not dummy:
        print(p.data, end=" ")
        p = inorder_successor(p)
