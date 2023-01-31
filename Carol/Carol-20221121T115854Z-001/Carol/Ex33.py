nu1 = float(input("Digite o 1°número:"))
nu2 = float(input("Digite o 2°número:"))
print("---------------------------")
print("---Operacões disponíveis---")
print("___________________________")
print("-------(+) para somar------")
print("-------(-) para subtrair---")
print("-------(*) para multiplicar")
print("-------(/) para dividir----")
print("___________________________")
op = str(input("Qual operação deseja reallizar?"))

# Calculadora

def checar():

    if (resultado_operacao // 1 == resultado_operacao):
        print("Inteiro")

        if resultado_operacao >= 0:
             print("positive")

             if resultado_operacao % 2 == 0:
                 print("{} é par ")

             else:
                print("é impar")

        else:
            print(" é negativo")

    else:
        print("é Decimal")

if op == '+':
    resultado_operacao = nu1+nu2
    print("Resultado",resultado_operacao)
    checar()
elif op == '-':
    resultado_operacao = nu1-nu2
    print("Resultado",resultado_operacao)
    checar()
elif op == '*':
    resultado_operacao = nu1*nu2
    print("Resultado",resultado_operacao)
    checar()
elif op == '/':
    resultado_operacao = nu1/nu2
    print("Resultado",resultado_operacao)
    checar()
else:
    print("Valor Inválido")