pao = (float(input("Digite a quantia de Pães vendidos:")))
broa = (float(input("Digite a quantia de Broas vendidas:")))

p = 1*pao
b = 3.5*broa
cont = (p+b)
arr = (cont*10)/100

print("O total arrecadado com pães e broas foram R$: {} \nA quantia a ser guardada é de R$: {}".format(cont, arr))