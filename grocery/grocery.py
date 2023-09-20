lista = dict()
while True:
    try:
        item = input("").upper().strip()
        if item not in lista:
            lista[item] = 1
        else:
            lista[item] += 1

    except EOFError:
        break

claves = sorted(lista.keys())
for item in claves:
    print(lista[item], item)
