cd = float(input("DIGITE O NUMERO DA SUA CONTA:"))
saldo = float(input("Digite o saldo:"))
debito = float(input("Digite o Débito:"))
credito = float(input("Digite o Crédito:"))

saldo_atual = (saldo-debito+credito)

if saldo_atual >= 0:
    print(f"Saldo positivo")
elif saldo_atual < 0 :
    print(f"Saldo negativo")
    print(f"A CONTA {cd} tem de saldo {saldo_atual}")