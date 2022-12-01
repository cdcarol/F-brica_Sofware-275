peso = float(input("Digite quantos quilos foram pescados:"))

if peso <= 50:
    fixo = 35
    print("o preço a ser cobrado é : R$35.00")

elif peso > 50:
    excesso = peso-50
    multa = excesso * 4
    fixo = 35 + multa
    print("Peso excesido:{} \nValor da multa:{}".format(excesso, multa))


