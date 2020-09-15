import random

# selecionar tipo de dado
print("Selecione um tipo de dado abaixo:\n")

print("A - para D4")
print("B - para D6")
print("C - para D8")
print("D - para D10")
print("E - para D12")
print("F - para D20")
print("Digite 'sair' ou '0' para finalizaro programa\n")

dado = str(input("Escolha de dado: "))
valor = 0
rolar = 1

# Rolagem do dado
while rolar == 1:
    if dado == "A" or dado == "a":
        valor = random.randint(1,4)
        print(valor)
        dado = str(input("Escolha de dado: "))
    elif dado == "B" or dado == "b":
        valor = random.randint(1,6)
        print(valor)
        dado = str(input("Escolha de dado: "))
    elif dado == "C" or dado == "c":
        valor = random.randint(1,8)
        print(valor)
        dado = str(input("Escolha de dado: "))
    elif dado == "D" or dado == "d":
        valor = random.randint(1,10)
        print(valor)
        dado = str(input("Escolha de dado: "))
    elif dado == "E" or dado == "e":
        valor = random.randint(1,12)
        print(valor)
        dado = str(input("Escolha de dado: "))
    elif dado == "F" or dado == "f":
        valor = random.randint(1,20)
        print(valor)
        dado = str(input("Escolha de dado: "))
    # condição de saída
    elif dado == "0" or dado == "sair":
        print("Deseja sair do programa?")
        resposta = str(input("Resposta(s/n): "))
        if resposta == "s" or "sim":
            rolar = 0
        else:
            dado = str(input("Escolha de dado: "))
#c condição de erro no input
    else:
        print("Dado escolhido de forma incorreta")
        dado = str(input("Escolha de dado: "))

# Programa encerrado
print("Programa encerrado\n")