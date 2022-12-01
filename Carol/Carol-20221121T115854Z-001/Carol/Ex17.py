salario = float(input("Digite sue salário:"))

if salario <= 280:
    salario_atual = salario+(salario*0.2)
    print(f"o aumento do salario foi de 20% ,seu novo salário é de: {salario_atual}")
elif 280 > salario  and salario <= 700:
    salario_atual = salario+(salario*0.15)
    print(f"o aumento do salario foi de 15%, seu novo salário é de: {salario_atual}")
if  700 > salario and salario <= 1500:
    salario_atual = salario+(salario*0.10)
    print(f"o aumento do salario foi de 10% ,seu novo salário é de: {salario_atual}")
elif 1500 >= salario:
    salario_atual = salario+(salario*0.5)
    print(f"o aumento do salario foi de 5% ,seu novo salário é de: {salario_atual}")