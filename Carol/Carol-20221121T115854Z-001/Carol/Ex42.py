l = float(input("Digite a quantia de refrigerantes de 350 ml: "))
ga = float(input("Digite a quantia de refrigerantes de 600 ml: "))
a = float(input("Digite a quantia de refrigerantes de 2l: "))

la = l*0.35
g = ga*0.60
ar = a*2

soma = la+g+ar

print("A quantidae de litros comprada foram: {}".format(soma))
print(" O litro do refrigerante de 350 ml : {}".format(la))
print(" O litro do refrigerante de 600 ml : {}".format(g))
print(" O litro do refrigerante de 2l : {}".format(ar))
