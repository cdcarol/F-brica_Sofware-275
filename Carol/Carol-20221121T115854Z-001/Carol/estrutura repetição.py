num = 0
soma = 0

while num != -999:
    soma += num
    num = float(input("Digite um número:"))

print("A soma dos números digitados foram: {}".format(soma))