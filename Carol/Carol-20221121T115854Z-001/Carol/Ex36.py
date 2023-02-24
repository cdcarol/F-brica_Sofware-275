cod = 0 
qtde = 0 
valor = 0 

print("-"*35) 
print("-Especificação----codigo---preço---") 
print("-Cachorro Quente---100----R$ 11.20-") 
print("-Ovo Simples    ---101----R$  8.30-") 
print("-Bauru com Ovo  ---102----R$ 11.50-") 
print("-Hamburguer     ---103----R$ 16.20-") 
print("-Refrigerante   ---201----R$  6.00-") 
print("-Suco           ---202----R$  7.50-") 
print("-Água Mineral   ---203----R$  4.70-") 
print("-"*35) 
cod = int(input(" informe o codigo:")) 
 
if cod == 100: 
   qtde = int(input("informe a quantidade: ")) 
   valor = 11.20 * qtde 
   print(f"o valor a ser pago:   {valor}") 
 
elif cod == 101: 
    qtde = int(input("informe a quantidade: ")) 
    valor = 8.30 * qtde 
    print("o valor a ser pago:  ", valor) 

elif cod == 102: 
    qtde = int(input("informe a quantidade: ")) 
    valor = 11.50 * qtde 
    print("o valor a ser pago:  ", valor) 

elif cod == 103: 
    qtde = int(input("informe a quantidade: ")) 
    valor = 16.20 * qtde 
    print ("o valor a ser pago:  ", valor) 
 
elif cod == 201: 
    qtde = int(input("informe a quantidade")) 
    valor = 6* qtde 
    print("o valor a ser pago:  ", valor) 

elif cod == 202: 
    qtde = int(input("informe a quantidade")) 
    valor = 7.5 * qtde 
    print("o valor a ser pago:  ", valor) 

elif(cod == 203): 
    qtde = int(input("informe a quantidade:")) 
    valor = 4.7 * qtde 
    print("o valor a ser pago:  ", valor) 