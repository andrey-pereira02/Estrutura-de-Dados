def linear_search(value, arr, n):
    for i in range(0, n):
        if arr[i] == True:
            return True


"""
    Esse laço é bom para analisarmos que ele pode executar só 1 vez se o primeiro valor for o procurado
    assim como pode executar n vezes se não tivermos sorte
"""

# Vamos comparar o algoritmo de cima com o a seguir:


def find_max(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


"""
    Você pode pensar que os dois são iterativos que possuem o mesmo tempo certo ? Errado
    O segundo algoritmo sempre vai executar n vezes e ponto final, nele não existe a sorte,
    pois ele obrigatoriamente tem que varrer o arr para encontrar o maior, enquanto o primeiro
    pode simplesmente na primeira iteração achar o que estava buscando
"""
