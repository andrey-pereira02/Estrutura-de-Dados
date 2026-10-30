def remove_element(heap, i):
    if i < 0 or i >= len(heap):
        raise IndexError("Índice inválido")

    ultimo = heap.pop()

    if i == len(heap):
        return

    heap[i] = ultimo

    parent = (i - 1) // 2

    # Se for menor que o pai, precisa subir
    if i > 0 and heap[i] < heap[parent]:

        while i > 0:
            parent = (i - 1) // 2

            if heap[i] >= heap[parent]:
                break

            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent

    # Caso contrário, verifica se precisa descer
    else:
        n = len(heap)

        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and heap[left] < heap[smallest]:
                smallest = left

            if right < n and heap[right] < heap[smallest]:
                smallest = right

            if smallest == i:
                break

            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
