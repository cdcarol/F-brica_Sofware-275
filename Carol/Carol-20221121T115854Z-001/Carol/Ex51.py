num = float(input("Digite um número: "))
soma = 0

while num != -999:
    soma += num
    num = float(input(""))

print("A soma dos números é: {}".format(soma))