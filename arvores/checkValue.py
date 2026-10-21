def checkValue(root, value):
    if root is None:
        return False

    if root.data == value:
        return "Sim, o valor "+value+" esta na arvore"

    return checkValue(root.left, value) or checkValue(root.right, value)
