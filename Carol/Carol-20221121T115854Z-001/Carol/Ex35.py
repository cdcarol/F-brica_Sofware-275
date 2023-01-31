tipo = int(input("Digite (1) para Filé Duplo, (2) para Alcatra e (3) para Picanha:"))
qdade = float(input("Digite quantos quilos: "))

if tipo == 1 :
    carne = "Filé"
    file = 34.90
    file5 = 35.80
    if qdade <= 5 :
        preco = qdade * file
    else:
        preco = qdade * file5
elif tipo == 2 :
    carne = "Alcatra"
    file = 44.90
    file5 = 46.80
    if qdade <= 5 :
        preco = qdade * file
    else:
        preco = qdade * file5
elif tipo == 3 :
    carne = "Picanha"
    file = 66.90
    file5 = 67.80
    if qdade <= 5 :
        preco = qdade * file

    else:
        preco = qdade * file5

resposta = str(input("A compra é realizada com Cartão Tabajara?, (Sim) (Não): "))

if resposta == 1 :
    desconto = preco * 0.05
    total = preco - desconto

else:
    total = preco

print("#" * 27)
print("#######Cupom Fiscal########")
print("#Carne_____________R$ {}#".format(file))
print("#Quilos______________{}kg#".format(qdade))
print("#Preço Total______R$ {}#".format(preco))
print("#Cartao Tabajara______ {}#".format(resposta))
print("#Desconto_________R$ {}#".format(total))
print("#Total a Pagar____R$ {}#".format(total))
print("#" * 27)