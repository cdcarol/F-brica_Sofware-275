aq = float(input("Digite o valor de aquisição do produto:"))

porm = aq+(aq*45) /100
por = aq+(aq*30) /100

if aq <= 50:
    print("o valor de venda é:{}".format(porm))
elif aq > 50:
    print("o valor de venda é:{}".format(por))