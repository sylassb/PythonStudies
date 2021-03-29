# University project of a TechFarm where I should use binary search to find cows in a specific list and know if it was milked or not and also if it is on the list: 

cows = [100, 101, 102, 103, 104, 105]
milkedCow = {100: 'Milked', 101: 'Not Milked', 102: 'Milked', 103: 'Milked', 104: 'Milked', 105: 'Milked'}

searchCow = int(input('Type the number of the cow you want to find: '))

def buscarVaca(list, item):
    prim = 0
    ult = len(list) - 1
    found = False
    resultFalse = f'The cow {item} was not found'
    resultTrue = f' The cow {item} was found'

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
