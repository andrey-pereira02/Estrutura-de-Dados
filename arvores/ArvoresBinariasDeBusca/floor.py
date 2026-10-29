def floor(root, key):
    candidate = None
    current = root

    while current:
        if current.value == key:
            return current.value

        elif current.value < key:
            candidate = current.value
            current = current.right

        else:
            current = current.left
