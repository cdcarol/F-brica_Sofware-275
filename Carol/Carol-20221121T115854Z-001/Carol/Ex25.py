#variavel
p = float(input("Digite a quantidade de camisetas pequenas:"))
m = float(input("Digite a quantidade de camisetas Médias:"))
g = float(input("Digite a quantidade de camisetas Grandes:"))

#Conta

pe = 10*p
me = 12*m
gr = 15*g
cont = (pe+me+gr)

#tela

print("valor toal de camisas pequenas:{} \nvalor toal de camisas Médias:{} \nvalor toal de camisas Grandes:{} \nO valor total da compra é:{}".format(pe, me, gr, cont))