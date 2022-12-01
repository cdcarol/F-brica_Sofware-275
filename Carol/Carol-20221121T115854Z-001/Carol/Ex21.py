fixo = float(input("Digite o valor do salário:"))
vendas = float(input("Digite o valor das vendas:"))

comi = (vendas*4) /100
sf = comi+fixo

print("sua comissão é de :{}\n seu salário final é :{}".format(comi, sf))