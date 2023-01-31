n = int(input("Digite o número referente a tabuada: "))
aux = 0

print('*' * 18)
print('Tabuada de {}'.format(n))
print('*' * 18)

while aux <= 10 :
    print("{0} x {1} = {2}".format(aux, n , (aux * n)))
    aux = aux + 1