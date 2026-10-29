def kEsimoMax(root, pos):
    if root is None:
        return None

    elements = []

    def onorder(root):
        if root is None:
            return None

        onorder(root.right)
        elements.append(root)
        onorder(root.left)

    onorder(root)

    if pos < 1 or pos > len(elements):
        return None
    return elements[pos - 1]
