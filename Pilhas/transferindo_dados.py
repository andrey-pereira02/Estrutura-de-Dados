from pilhas_arraySimples import *


def transferindoDados(pilhaS: Stack, pilhaT: Stack):
    if pilhaS.isEmpTy():
        return "Stack Vazia"

    qtn = pilhaS.top + 1
    pilhaT.A = [None] * qtn

    for i in range(qtn):
        pilhaT.push(pilhaS.A[pilhaS.top])
        pilhaS.top -= 1
