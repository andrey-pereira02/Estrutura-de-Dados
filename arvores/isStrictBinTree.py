def isStrictBinTree(root):
    """Algoritmo de arvore propria"""
    if not root:
        return False

    if (root.left is None and root.right) or (root.right is None and root.left):
        return False

    return isStrictBinTree(root.right) and isStrictBinTree(root.left)
