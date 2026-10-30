
class MinHeap:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] >= self.heap[parent]:
                break

            self.heap[index], self.heap[parent] = (
                self.heap[parent], self.heap[index]
            )

            index = parent

    def _heapify_down(self, index):
        n = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest], self.heap[index]
            )

            index = smallest

    def remove_min(self):
        if not self.heap:
            raise IndexError("Heap vazio")

        minimum = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)

        return minimum

    def get_min(self):
        if not self.heap:
            raise IndexError("Heap vazio")

        return self.heap[0]


class MaxHeap:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] <= self.heap[parent]:
                break

            self.heap[index], self.heap[parent] = (
                self.heap[parent], self.heap[index]
            )

            index = parent

    def _heapify_down(self, index):
        n = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = (
                self.heap[largest], self.heap[index]
            )

            index = largest

    def remove_max(self):
        if not self.heap:
            raise IndexError("Heap vazio")

        maximum = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)

        return maximum

    def get_max(self):
        if not self.heap:
            raise IndexError("Heap vazio")

        return self.heap[0]
