def minABB(root):
    if root is None:
        return

    if root.left:
        return minABB(root.left)
    return root
