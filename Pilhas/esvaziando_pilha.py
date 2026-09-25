from pilhas_arraySimples import *


def esvaziando_pilha(pilha: Stack):
    if pilha.isEmpTy():
        return "Já esta vazia"

    while pilha.isEmpTy() == False:
        pilha.pop()

    return "Pilha esvaziada"


def Empty(pilha: Stack):
    if pilha.isEmpTy():
        return True

    pilha.pop()

    Empty(pilha)
