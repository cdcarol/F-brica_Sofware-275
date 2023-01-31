number = int(input(" Fatorial de: "))
resultado = 1
cont = 1

while cont <= number:
    resultado *= cont
    cont += 1
    print(resultado)

print("Fatorial de {}! é {}".format(number, resultado))


