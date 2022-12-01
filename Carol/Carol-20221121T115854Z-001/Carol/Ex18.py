hora= float(input("Digite o valor da sua hora:"))
qh = float(input("Digite quantas horas foram trabalhadas:"))

salario_bruto = hora*qh

if salario_bruto <= 900:
   sindicato = salario_bruto*0.03
   inss = salario_bruto*0.1
   fgts = salario_bruto*0.11
   salario_liquido = salario_bruto - sindicato - inss
   print(f"O valor do salário bruto: R${salario_bruto:.2f}")
   print(f"O valor do sindicato    : R${sindicato:.2f}")
   print(f"O valor do inss         : R${inss:.2f}\n")
   print(f"O valor do salario líquido é: R${salario_liquido:.2f}")
   print(f"O valor do fgts depositado em conta é: R$  {fgts:.2f}")


elif 900 > salario_bruto and salario_bruto <=1500:
     ir = salario_bruto*0.05
     sindicato = salario_bruto*0.03
     inss = salario_bruto*0.1
     fgts = salario_bruto*0.11
     salario_liquido = salario_bruto - sindicato - inss - ir
     print(f"O valor do salário bruto: R${salario_bruto:.2f}")
     print(f"O valor do sindicato    : R${sindicato:.2f}")
     print(f"O valor do ir           : R${ir:.2f}")
     print(f"O valor do inss         : R${inss:.2f}\n")
     print(f"O valor do salario líquido é: R${salario_liquido:.2f}")
     print(f"O valor do fgts depositado em conta é: R$  {fgts:.2f}")

if 1500 > salario_bruto and salario_bruto <= 2500:
   ir = salario_bruto*0.1
   sindicato = salario_bruto*0.3
   inss = salario_bruto*0.11
   fgts = salario_bruto*0.1
   salario_liquido = salario_bruto - sindicato - inss - ir
   print(f"O valor do salário bruto: R${salario_bruto:.2f}")
   print(f"O valor do sindicato    : R${sindicato:.2f}")
   print(f"O valor do ir           : R${ir:.2f}")
   print(f"O valor do inss         : R${inss:.2f}\n")
   print(f"O valor do salario líquido é: R${salario_liquido:.2f}")
   print(f"O valor do fgts depositado em conta é: R$  {fgts:.2f}")

elif salario_bruto > 2500:
   ir = salario_bruto*0.2
   sindicato = salario_bruto*0.3
   inss = salario_bruto*0.11
   fgts = salario_bruto*0.1
   salario_liquido = salario_bruto - sindicato - inss - ir
   print(f"O valor do salário bruto: R${salario_bruto:.2f}")
   print(f"O valor do sindicato    : R${sindicato:.2f}")
   print(f"O valor do ir           : R${ir:.2f}")
   print(f"O valor do inss         : R${inss:.2f}\n")
   print(f"O valor do salario líquido é: R${salario_liquido:.2f}")
   print(f"O valor do fgts depositado em conta é: R$  {fgts:.2f}")
