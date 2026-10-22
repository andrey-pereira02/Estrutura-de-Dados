def heightBinTree(root):
    if root is None:
        return -1

    if root.left is None and root.right is None:
        return 0

    return 1 + max(heightBinTree(root.left), heightBinTree(root.right))
