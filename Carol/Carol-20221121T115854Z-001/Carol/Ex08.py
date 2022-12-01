com = float(input("Digite o valor a ser gasto com o Combustível:"))
ped = float(input("Digite o valor a ser gasto com pedágios:"))
ali = float(input("Digite o valor estimado a ser gasto com alimentação:"))
hos = float(input("Digite o valor a ser gasto com Hospedagem:"))
soma = (com+ped+ali+hos)

print(" Valor gasto com o Combustível: {}\n, Valor gasto com os Pedágios: {}\n, Valor gasto com Alimentação: {}\n, Valor gasto com a Hospedagem: {}".format(com, ped, ali, hos))
print("O valor total estimado é: ", soma)