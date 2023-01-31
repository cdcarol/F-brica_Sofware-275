lista = [10, 20, 30, 40, 50, 60]
[print(num) for num in lista]

# Com enumerate:
[print(f'índice={indice}, valor={valor}') for indice, valor in enumerate(lista)]