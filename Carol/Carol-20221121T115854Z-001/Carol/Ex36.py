print("_" * 20)
print("|Especificação  |Código|Preço  |")
print("|Cachorro Quente|100   |R$11.20|")
print("|Ovo Simples    |101   |R$ 8.30|")
print("|Bauru com Ovo  |102   |R$11.50|")
print("|Hanbúrguer     |103   |R$16.20|")
print("|Refrigerante   |201   |R$ 6.00|")
print("|Suco           |202   |R$ 7.50|")
print("|Água Mineral   |203   |R$ 4.70|")
print("_"* 20 )

cod = int(input("Digite o Código de seu Lanche: "))
codb = int(input("Digite o Código da sua Bebida: "))

if cod == 100 :
    quente = 11.20
