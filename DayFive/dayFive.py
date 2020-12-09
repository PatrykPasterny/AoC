import math
############### FIRST PART OF PUZZLE #################

def readfile(name):
        with open(name) as myFile:
            return myFile.read()

def getId(row, col):
    return 8 * row + col 

def firstPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayFive/input.txt")

    seatCodes = [x for x in readMyFile.split('\n') if x != '']
    rowCodes = [x[:-4] for x in seatCodes]
    colCodes = [x[6:] for x in seatCodes]
    
    seatCodesToNums = []
    for seat in seatCodes:
        rowNum = 0
        for i, ch in enumerate(seat[6::-1]):
            if 'B' in ch.upper():
                
                rowNum += pow(2, i)

        colNum = 0
        for i, ch in enumerate(seat[:-4:-1]):
            if 'R' in ch.upper():
                colNum += pow(2, i)
        
        seatCodesToNums.append({'row': rowNum, 'col': colNum})
    
    seatIds = [getId(x['row'], x['col']) for x in seatCodesToNums]
    print(max(seatIds))

    return seatIds

#####SECOND PART OF PUZZLE########

def inRange(num, start, end):
    return num >= start and num <= end

def secPart():
    seatIds = firstPart()

    lackingSeatIds = []
    for i in range(max(seatIds)):
        if i not in seatIds and (i - 1) in seatIds and (i + 1) in seatIds:
            lackingSeatIds.append(i)

    print(lackingSeatIds)
    
if __name__ == "__main__":
    firstPart()
    secPart()