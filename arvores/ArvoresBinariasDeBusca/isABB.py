def inorder(root):
    if root is None:
        return []

    elements = []
    elements += inorder(root.left)
    elements.append(root.value)
    elements += inorder(root.right)

    return elements


def isABB(root):
    elements = inorder(root)

    for i in range(1, len(elements)):
        if elements[i - 1] >= elements[i]:
            return False

    return True
