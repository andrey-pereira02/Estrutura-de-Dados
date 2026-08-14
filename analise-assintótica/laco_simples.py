n = int(input("Digite um numero: "))

for i in range(0, n):
    print(i)
"""
    Esse laço simples tem um tempo e O(n), pois ele executara n vezes
"""

for k in range(0, n):
    for j in range(0, n):
        print(i)
"""
    Esse laço possui o tempo de O(n²), pois tem um laço dentro de outro e ambos vão fazer n iterações
"""
