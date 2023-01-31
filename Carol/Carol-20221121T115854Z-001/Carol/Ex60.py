n = int(input("Digite o número para ver a tabuada: "))

aux = 0

print("Tabuada do {}".format(n))

while aux <= 10 :
    print("{0} x {1} = {2}".format(aux, n, (aux * n)))
    aux = aux + 1