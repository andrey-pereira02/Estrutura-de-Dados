from Heaps import *


def maxElement(minHeap):
    if minHeap is None:
        return False

    inicio = len(minHeap)//2

    return max(minHeap[inicio:])
