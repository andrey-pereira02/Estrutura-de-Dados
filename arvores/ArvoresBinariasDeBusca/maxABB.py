def maxABB(root):
    if root is None:
        return

    if root.right:
        return maxABB(root.right)
    return root
