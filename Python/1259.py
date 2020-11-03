n = int(input())
pares = []
impares = []
ordenados = []
for i in range(0, n, 1):
    aux = int(input())
    if aux % 2 == 0:
        pares.append(aux)
    else:
        impares.append(aux)

pares.sort()
impares.sort(reverse=True)
ordenados = pares + impares
for num in ordenados:
    print(num)