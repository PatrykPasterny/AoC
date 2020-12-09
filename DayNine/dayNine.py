def doAnyTwoNumbersInArraySumToGivenNum(numsToSum, resultNum):
    for num1 in numsToSum:
        for num2 in numsToSum:
            if num1 + num2 == resultNum:
                return True
    
    return False

def readfile(name):
        with open(name) as myFile:
            return myFile.read()

############### FIRST PART OF PUZZLE #################

def firstPart(preambleLength):
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayNine/input.txt")

    XMASCypherList = [int(number) for number in readMyFile.split('\n') if number != '']
    cypherLength = len(XMASCypherList)
    if cypherLength < preambleLength:
        return -1
    else:
        for idx, number in enumerate(XMASCypherList[preambleLength:]):
            numbersToSum = XMASCypherList[idx:idx + preambleLength]
            if not doAnyTwoNumbersInArraySumToGivenNum(numbersToSum, number):
                return number
        
        return -1

def secPart(preambleLength):
    invalidNumber = firstPart(preambleLength)

    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayNine/input.txt")
    XMASCypherList = [int(number) for number in readMyFile.split('\n') if number != '']
    
    for idx, number in enumerate(XMASCypherList):
        contigousSetSum = 0
        contigousSetLength = 2
        while contigousSetSum < invalidNumber:
            numbersToSum = XMASCypherList[idx:idx + contigousSetLength]
            contigousSetSum = sum(numbersToSum)
            if contigousSetSum == invalidNumber:
                print(numbersToSum)
                return max(numbersToSum) + min(numbersToSum)
            
            contigousSetLength += 1


if __name__ == "__main__":
    print(firstPart(25))
    print(secPart(25))