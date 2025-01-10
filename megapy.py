from random import randint

dezenas: int = int(input("Quantas dezenas deseja marcar? "))
qtd_jogos: int = int(input("Quantos jogos deseja fazer? "))
alfabeto = 65

if (dezenas <= 20 and dezenas >=6 ) and qtd_jogos > 0:
    for _ in range(qtd_jogos):
        numeros = []
        while len(numeros) < dezenas:
            numero = randint(1,60)
            if numero not in numeros:
                numeros.append(numero)
        numeros.sort()
        
        print(f'JOGO {chr(alfabeto)} - {numeros}')
        alfabeto += 1
else:
    print("A quantidade de números jogados (dezenas) deve ser entre 6 e 20 e"
          " a quantidade de jogos deve ser de no mínimo 1.")