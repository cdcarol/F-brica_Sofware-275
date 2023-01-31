nascido = int(input("Digite o ano em que nasceu: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - nascido
ano = idade * 365
mes = idade * 12
semanas = mes / 7
dias = mes * 30

print("Dias {}, Semanas {}, Meses {}, Anos {}.".format(dias, semanas, mes, idade))