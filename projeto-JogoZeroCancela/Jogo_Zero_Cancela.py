somaTotal = 0
numCon = 0
numDes = 0
ultimo_num_1 = 0
ultimo_num_2 = 0
ultimo_num_3 = 0
ultimo_num_4= 0
zero_consecutivo = 0
print("_"*50)
print("\tBem-vindo ao jogo do Zero cancela!")
print("_"*50 )
num = int(input('\nDigite um número: '))
while num >= 0:

    if num > 0:
        numCon += 1
        somaTotal += num
        ultimo_num_4 = ultimo_num_3
        ultimo_num_3 = ultimo_num_2
        ultimo_num_2 = ultimo_num_1
        ultimo_num_1 = num
        zero_consecutivo = 0  

    elif num == 0:
        zero_consecutivo += 1
        numCon -= 1
        if zero_consecutivo == 1:
            somaTotal -= ultimo_num_1
            ultimo_num_1 = ultimo_num_2
            ultimo_num_2 = ultimo_num_3
            ultimo_num_3 = ultimo_num_4
            ultimo_num_4= 0
            numDes += 1

        elif zero_consecutivo == 2:
            somaTotal -= ultimo_num_1
            ultimo_num_1 = ultimo_num_2
            ultimo_num_2 = ultimo_num_3
            ultimo_num_3=0
            ultimo_num_4=0
            numDes += 1

        elif zero_consecutivo == 3:
            somaTotal -= ultimo_num_1
            ultimo_num_1 = ultimo_num_2
            ultimo_num_2 = 0
            ultimo_num_3 = 0
            ultimo_num_4=0
            numDes += 1

        else:
            numCon+=1
            print('Só é permitido no máximo 3 zeros consecutivos')
    num = int(input('\nDigite um número: '))
print("_"*50)
print("\n\tZero cancela finalizado!")
print("_"*50)
print("\t\nSoma Total: ", somaTotal)
print("\t\nNúmeros considerados na soma: ", numCon)
print("\t\nNúmeros desconsiderados: ", numDes)
print("_"*50)
print("_"*50)