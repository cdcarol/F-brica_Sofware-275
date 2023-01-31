num = float(input("Digite um número: "))

menor = num
maior = num
soma = 0

while num != -999 :
    soma += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    num = float(input(""))
print(" A soma dos números digitados foi: {}.\n O menor número digitado foi: {}.\n O maior número digitado:{}".format(soma, menor, maior))