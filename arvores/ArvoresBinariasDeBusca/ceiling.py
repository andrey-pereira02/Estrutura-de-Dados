def ceiling(root, key):
    candidate = None
    current = root

    while current:
        if current.value == key:
            return current.value

        elif current.value > key:
            candidate = current.value
            current = current.left

        else:
            current = current.right
