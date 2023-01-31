u = float(input("Digite a quantidade de moedas de 1 centavo : "))
c = float(input("Digite a quantidade de moedas de 5 centavo : "))
d = float(input("Digite a quantidade de moedas de 10 centavo : "))
v = float(input("Digite a quantidade de moedas de 25 centavo : "))
q = float(input("Digite a quantidade de moedas de 50 centavo : "))
r = float(input("Digite a quantidade de moedas de 1 real : "))

um = 0.01*u
cinco = 0.05*c
dez = 0.1*d
vinte_cinco = 0.25*v
cinquenta = 0.5*q
real = 1*r
soma = um+cinco+dez+vinte_cinco+cinquenta+real

print("O valor economizado é de: R$ {}".format(soma))
