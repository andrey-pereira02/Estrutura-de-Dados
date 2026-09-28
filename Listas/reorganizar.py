from lista_encadeada import *


def reorganizar(head, previous, current, k: int):
    if current.proximo == None:
        return head

    if current.data <= k:

        if current == head:
            return reorganizar(head, previous, current.proximo, k)

        previous.proximo = current.proximo

        current.proximo = head
        head = current

        return reorganizar(head, previous, previous.proximo, k)

    return reorganizar(head, current, current.proximo, k)
