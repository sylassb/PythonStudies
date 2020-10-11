cows = [100, 101, 102, 103, 104, 105]
milkedCow = {100: 'Ordenhada', 101: 'Não Ordenhada', 102: 'Ordenhada', 103: 'Ordenhada', 104: 'Ordenhada', 105: 'Ordenhada'}

searchCow = int(input('Digite o número da vaca que você quer encontrar: '))

def buscarVaca(list, item):
    prim = 0
    ult = len(list) - 1
    found = False
    resultFalse = f'A vaca {item} não foi encontrada'
    resultTrue = f' A vaca {item} foi encontrada'

    while prim <= ult and not found:
        meio = (prim + ult) // 2
        if list[meio] == item:
            found = True
        else:
            if item < list[meio]:
                ult = meio - 1
            else:
                prim = meio + 1

    if found == True:
        return resultTrue
    else:
        return resultFalse

print(buscarVaca(cows, searchCow))
print(f'{milkedCow.get(searchCow)}')