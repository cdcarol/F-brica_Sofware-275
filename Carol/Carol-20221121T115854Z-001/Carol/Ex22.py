preco = float(input("Digite o preço do produto:"))

des = (preco*10) /100
cont = preco-des

print("Desconto de: {}\n o novo preço é: {}".format(des, cont))