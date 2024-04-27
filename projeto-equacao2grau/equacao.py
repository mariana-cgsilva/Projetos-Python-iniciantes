
print("Vamos calcular as raízes de uma equação de segundo grau.")
print("                 ax² + bx + c = 0")
print()

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

print()
print(f"A equação a ser calculada é: {a}x^2 + {b}x + {c} = 0")

def calculo():
    discriminante = (b ** 2) - (4 * a * c)

    if discriminante > 0:
        # Duas raízes reais distintas
        raiz1 = (-b + (discriminante ** 0.5)) / (2 * a)
        raiz2 = (-b - (discriminante ** 0.5)) / (2 * a)
        return raiz1, raiz2
    elif discriminante == 0:
        # Uma raiz real (raiz dupla)
        raiz = -b / (2 * a)
        return raiz,
    else:
        # Raízes complexas
        parte_real = -b / (2 * a)
        parte_imaginaria = ((-discriminante) ** 0.5) / (2 * a)
        return (parte_real, parte_imaginaria), (parte_real, -parte_imaginaria)


if a == 0:
    print("Não é uma equação de segundo grau.")
    a2 = int(input("Deseja digitar outro valor para a? (S/N)"))

    if a2 == 'S':
        a = int(input("Digite o novo valor para a: "))
        calculo()
    elif a2 == 'N':
        print("Você cancelou o cálculo das raízes da equação.")
    else: 
        print("Inserção inválida. Digite S para sim e N para não.") 
else: 
    raizes = calculo()
    print("As raízes da equação são:")
    for raiz in raizes:
        if isinstance(raiz, tuple):
            print(f"{raiz[0]} + {raiz[1]}i")
        else:
            print(raiz)



