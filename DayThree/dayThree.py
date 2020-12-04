from math import ceil

############### FIRST PART OF PUZZLE #################

def readfile(name):
        with open(name) as myFile:
            return myFile.read()

def firstPart(moveDown, moveRight):
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayThree/input.txt")
    
    singleMapLength = readMyFile.find('\n')
    mapHeight = len([x for x in readMyFile.split('\n') if x != ''])
    neededLength = ceil(float(mapHeight * moveRight) / float(moveDown * singleMapLength))
    map = [[ch for ch in (neededLength * x)] for x in readMyFile.split('\n') if x != '']


    sum = 0
    (i, j) = (0, 0)
    while i < mapHeight:
        if (map[i][j] is '#'):
            sum += 1
        
        i += moveDown
        j += moveRight
    print("For down: " + str(moveDown) + ", right: " + str(moveRight))
    print("MapHeight: " + str(mapHeight))
    print("SingleMapLength: " + str(singleMapLength))
    print("MapLength: " + str(singleMapLength * neededLength))
    print("i: " + str(i) + " j: " + str(j))
    print("Result: " + str(sum))
    return sum

def secPart():
    slopeTestCases = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    
    mult = 1
    for case in slopeTestCases:
        mult *= firstPart(case[0], case[1])

    print(mult)
    
if __name__ == __name__:
    firstPart(1, 3)
    secPart()