# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    return n1 / n2


print("\nSelecione o número para a operação desejada:\n")
print("1 – Soma\n2 – Subtração\n3 – Multiplicação\n4 – Divisão")

operacao = int(input("\nDigite sua operação (1,2,3,4):"))

if operacao == 1:
    print("\n**** Soma selecionada!!! ****")
    n1 = int(input("\nDigite o primeiro número: "))
    n2 = int(input("\nDigite o segundo número: "))
    somaNum = soma(n1, n2)
    print("\nResultado da operação:", somaNum)

elif operacao == 2:
    print("\n**** Subtração selecionada!!! ****")
    n1 = int(input("\nDigite o primeiro número: "))
    n2 = int(input("\nDigite o segundo número: "))
    sub = subtracao(n1, n2)
    print("\nResultado da operação:", sub)

elif operacao == 3:
    print("\n**** Multiplicação selecionada!!! ****")
    n1 = int(input("\nDigite o primeiro número: "))
    n2 = int(input("\nDigite o segundo número: "))
    mult = multiplicacao(n1, n2)
    print("\nResultado da operação:", mult)

else:
    print("\n**** Divsão selecionada!!! ****")
    n1 = int(input("\nDigite o primeiro número: "))
    n2 = int(input("\nDigite o segundo número: "))
    if n2 == 0:
        print("\nDivisão por zero detectada, operação cancelada!")
    else:
        div = divisao(n1, n2)
        print("\nResultado da operação:", div)
