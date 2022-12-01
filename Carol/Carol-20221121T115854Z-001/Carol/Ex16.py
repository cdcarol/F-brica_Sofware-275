n1 = (int(input("Digite o 1° número")))
n2 = (int(input("Digite o 2° número")))
n3 = (int(input("Digite o 3° número")))

if n1 < n2 and n1 < n3 :
    print(f"{n1} é menor do que {n2} e {n3}")
elif n1 > n2 and n1 > n3 :
    print(f"{n1} é menor que {n2} e {n3}")
if n2 < n1 and n2 < n3 :
    print(f"{n2} é menor do que {n1} e {n3}")
elif n1 > n2 and n2 > n3 :
    print(f"{n2} é maior que {n1} e {n3}")
if n3 < n1 and n3 < n2 :
    print(f"{n3} é menor que {n1} e {n2}")
elif n3 > n1 and n3 > n2 :
    print(f"{n3} é maior que {n1} e {n2}")