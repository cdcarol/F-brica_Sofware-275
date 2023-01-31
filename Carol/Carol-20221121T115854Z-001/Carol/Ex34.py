litro = float(input("Digite quantos litros desseja colocar:"))
com = str(input("Digite (A) para Álcool e (G) para Gasolina:"))

a = litro*1.9
g = litro*2.5

if com == "A":
    litro <= 20
    al = (a*3)/100
    print("o valor a ser pago pelo Álcool será R$ {}\n seu desconto é de {}".format(a, al))

elif litro > 20:
    al = (a*5)/100
    print("o valr a ser pago pelo Álcool será R$ {} \n seu desconto é de {}".format(a, al))



elif com == "G":
     litro <= 20
     ga = (g*4)/100
     print("o valor a ser pago pela Gasolina será R$ {} \n seu desconto é de {}".format(g, ga))

else:
    litro > 20
    ga = (g*6)/100
    print("o valor a ser pago pela Gasolina será: R$ {} \n seu desconto é de {}".format(g, ga))