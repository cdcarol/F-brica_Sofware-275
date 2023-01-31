import os, math

conta = float(input("Digite o valor do conta: "))
conta_para_Joceyr=math.floor(conta/3)
conta_para_thiago=conta_para_Joceyr
conta_para_alex=conta-conta_para_Joceyr-conta_para_thiago
print("O valor do conta para Thiago: " + repr(conta_para_thiago))
print("O valor do conta para Joceyr: " + repr(conta_para_Joceyr))
print("O valor do conta para Alexandre: " + repr(conta_para_alex))
print()
os.system('pause')