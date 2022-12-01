nome = input("Digite seu nome:")
idade = float(input("Digite sua idade:"))

if idade <= 2:
    print(f"{nome} é um bebê")
elif 3 <= idade and idade <= 11:
    print(f"{nome} é uma criança")
if 12 <= idade and idade <= 21:
    print(f"{nome} é jovem")
elif 22 <= idade and idade <= 64:
    print(f"{nome} é um adulto")
if 65 <= idade and idade <= 100:
    print(f"{nome} é um idoso")
elif idade >= 101:
    print(f"{nome} é muito velinho")