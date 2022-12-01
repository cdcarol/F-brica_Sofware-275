nome = input("Digite seu nome:")
Dis = input("DIgite a Disciplina:")
A = float(input("Digite a 1° nota"))
B = float(input("Digite a 2° nota"))
C = float(input("Digite a 3° nota"))
Media = (A+B+C)/3
if(Media >= 6):
    print(f"As notas foram:\n {A}, {B}, {C} Media do "
          f"aluno {nome} foi {Media:.1f}, foi o suficiente para passar.")
else:
    print(f"As notas foram:\n {A}, {B}, {C} a Media do "
          f"aluno {nome} foi {Media:.1f}, Não foi o suficiente para passar.")