print("Valor máximo R$ 600 \nValor mínimo R$ 10")
nu = int(input("Digite o valor a ser sacado R$: "))

cem = int(nu / 100)
nu = nu - (cem*100)

cinquenta = int(nu / 50)
nu = nu - (cinquenta*50)

dez = int(nu / 10)
nu = nu - (dez*10)

cinco = int(nu / 5)
nu = nu - (cinco*5)

um = nu

print("Notas de R$ 100,00: ", cem)
print("Notas de R$  50,00: ", cinquenta)
print("Notas de R$  10,00: ", dez)
print("Notas de R$    5,0: ", cinco)
print("Notas de R$    1,0: ", um)