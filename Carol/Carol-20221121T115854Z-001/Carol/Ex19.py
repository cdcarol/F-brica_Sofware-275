a = float(input("Digite o 1° lado:"))
b = float(input("Digite o 2° lado:"))
c = float(input("Digite o 3° lado:"))

if (a+b<c) or (a+c<b) or (b+c<a) :
    print("não é um triangulo")

elif (a==b) and (a==c):
    print("Equilátero")

elif (a==b) or (a==c) or (b==c) :
    print("Isóceles")

else:
    print("Escaleno")