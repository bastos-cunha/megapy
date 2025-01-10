from random import randint

dezenas: int = int(input("Quantas dezenas deseja marcar? "))
qtd_jogos: int = int(input("Quantos jogos deseja fazer? "))

for _ in range(qtd_jogos):
    numeros = []
    while len(numeros) < dezenas:
        numero = randint(1,60)
        if numero not in numeros:
            numeros.append(numero)
    numeros.sort()
    print(numeros)