def isCompleteBinTree(root):
    """Algorimto de arvore cheia"""
    if not root:
        return False

    if (bool(root.left) != bool(root.right)) or (root.left is None and root.right is None):
        return False

    return (isCompleteBinTree(root.left), isCompleteBinTree(root.right))
