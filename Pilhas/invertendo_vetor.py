from pilhas_arraySimples import *


def inverte_vetor(pilha: Stack, vetor=[]):
    if len(vetor) == 0:
        return "Vetor Vazio"

    tam = len(vetor)

    for i in vetor:
        pilha.push(vetor[i])

    for k in range(tam):
        vetor[i] = pilha.pop()
