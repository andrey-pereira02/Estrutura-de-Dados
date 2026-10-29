def kEsimoMin(root, pos):
    if root is None:
        return None

    elements = []

    def inorder(root):
        if root is None:
            return

        inorder(root.left)
        elements.append(root)
        inorder(root.right)

    inorder(root)

    if pos < 1 or pos > len(elements):
        return None
    return elements[pos - 1]
