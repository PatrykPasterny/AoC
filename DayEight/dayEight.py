import re

class Operation:

    def __init__(self, operationLine):     
        operationReg = re.compile(r"^(acc|jmp|nop)\s(\+?)(\-?\d+)$")
        operationRes = operationReg.search(operationLine)
        self.operationName = operationRes.group(1)
        self.operationInput = int(operationRes.group(3))

def readfile(name):
        with open(name) as myFile:
            return myFile.read()

def runOperation(operationToPerform):
    if ("nop" in operationToPerform.operationName):
        return (0, 1)
    elif ("jmp" in operationToPerform.operationName):
        return (0, operationToPerform.operationInput)
    else:
        return (operationToPerform.operationInput, 1)
    
############### FIRST PART OF PUZZLE #################

def firstPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayEight/input.txt")

    operationsList = [Operation(op) for op in readMyFile.split('\n') if op != '']
    
    accCount = 0
    index = 0
    firstOperation = operationsList[index]
    alreadyPerformedActions = set([index])
    (accIncrease, indexIncrease) = runOperation(firstOperation)
    index += indexIncrease

    while index not in alreadyPerformedActions:
        alreadyPerformedActions.add(index)
        accCount += accIncrease
        secOperation = operationsList[index]
        (accIncrease, newIndex) = runOperation(secOperation)
        index += newIndex
    
    return accCount
    
def secPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayEight/input.txt")

    operationsListMutable = [Operation(op) for op in readMyFile.split('\n') if op != ''] 
    operationsList = [Operation(op) for op in readMyFile.split('\n') if op != ''] 

    for idx, op in enumerate(operationsListMutable):
        operationNameToSwitch = op.operationName
        if "nop" in op.operationName:
            operationsList[idx].operationName = "jmp"
        elif "jmp" in op.operationName:
            operationsList[idx].operationName = "nop"
        else:
            continue

        indexValidator = len(operationsList)
        accCount = 0
        index = 0
        firstOperation = operationsList[index]
        alreadyPerformedActions = set([index])
        (accIncrease, indexIncrease) = runOperation(firstOperation)
        index += indexIncrease

        while index not in alreadyPerformedActions:
            alreadyPerformedActions.add(index)
            accCount += accIncrease
            secOperation = operationsList[index]
            (accIncrease, newIndex) = runOperation(secOperation)
            index += newIndex
            if index == indexValidator:
                return accCount + accIncrease
        
        operationsList[idx].operationName = operationNameToSwitch

if __name__ == "__main__":
    print(firstPart())
    print(secPart())

