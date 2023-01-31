num = float(input("Digite um número: "))
maior = num
menor = num

for i in range (1,20):
    num = float(input("Digite outro número: "))
    if num < menor :
        menor = num
    if num > maior :
        maior = num

print("O menor número digitado foi: {}".format(menor))
print("O maior número digitado foi: {}".format(maior))