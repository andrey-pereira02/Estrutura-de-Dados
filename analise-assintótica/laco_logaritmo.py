n = int(input("Digite um numero: "))
i = n

while (i > 0):
    i /= 2
    print("Valor de i ", i)

"""
    Isso é oq chamamos de laço logaritmo, pois a cada iteração o i é dividido por 2
    matematicamente seria assim : 
        n=2^m, i ficaria 2^m,2^m-1,2^m-2,...,2,1,0
"""

while (i < 100):
    i *= 2
    print(i)

"""
    Esse exemplo tem a mesma logica do outro, mas nesse caso estamos multiplicando por 2
    oq matematicamente ficaria assim:
        n=2^k, i ficaria 2;2^2;2^3 .....
"""

"""
    Em ambos os casos dizemos que o tempo desses algoritmos é O(log n)
"""
