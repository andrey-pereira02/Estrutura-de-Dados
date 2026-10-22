def isFullBinTree(root):
    if not root:
        return False

    if (root.left is None and root.right) or (root.right is None and root.left):
        return False

    return isFullBinTree(root.right) and isFullBinTree(root.left)
