def lowestCommonAnscestor(root, p, q):
    current = root

    while current:
        if p < current.value and q < current.value:
            current = current.left

        elif p > current.value and q > current.value:
            current = current.right

        else:
            return current
