import re

class bagRule:
    def __init__(self, bagRuleLine):
        self.bagContains = dict()
        bNameReg = re.compile(r"^([a-z]+\s[a-z]+)")
        bNameRes = bNameReg.search(bagRuleLine)
        self.bagName = bNameRes.group(0)
        bContArr = re.findall(r"[1-9]+\s[a-z]+\s[a-z]+", bagRuleLine)
        for bag in bContArr:
            contBagNumReg = re.compile(r"^([1-9]+)(\s)([a-z]+\s[a-z]+)$")
            contBagNumRes = contBagNumReg.search(bag)
            if (contBagNumRes):
                self.bagContains[contBagNumRes.group(3)] = contBagNumRes.group(1)
    
def findAllBagsContaining(bagsDictsArr, bagName):
    return [bag.bagName for bag in bagsDictsArr if bagName in bag.bagContains]

def findAllLevelBagsContaining(bagsDictsArr, bagName, resultSet):
    currLevelBags = findAllBagsContaining(bagsDictsArr, bagName)
    if len(currLevelBags) == 0:
        return bagName
    else:
        for bag in currLevelBags:
            resultSet.append(bag)
            resultSet.append(findAllLevelBagsContaining(bagsDictsArr, bag, resultSet))

def findAllBagsInside(bagsDictsArr, currentBag):
    return [bagDict for bagDict in bagsDictsArr if bagDict.bagName in currentBag.bagContains.keys()]

def findNumberOfAllLevelBagsInside(bagsDictsArr, currentBag, bagsOnLevel):
    currLevelBags = findAllBagsInside(bagsDictsArr, currentBag)
    if len(currLevelBags) == 0:
        return bagsOnLevel
    else:
        result = 0
        for bag in currentBag.bagContains:
            currBagDict = next(bagDict for bagDict in currLevelBags if bagDict.bagName in bag)
            result += findNumberOfAllLevelBagsInside(bagsDictsArr, currBagDict, bagsOnLevel * int(currentBag.bagContains[bag]))
        
        return result + bagsOnLevel

def readfile(name):
        with open(name) as myFile:
            return myFile.read()

############### FIRST PART OF PUZZLE #################

def firstPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DaySeven/input.txt")

    bagRulesData = [bagRule(bagRuleLine) for bagRuleLine in readMyFile.split('\n') if bagRuleLine != '']
    allLevelBagsWithShinyGold = []
    findAllLevelBagsContaining(bagRulesData, "shiny gold", allLevelBagsWithShinyGold)
    allLevelBagsWithShinyGold.remove(None)
    dupa = set(allLevelBagsWithShinyGold)
    dupa.remove(None)
    print(len(set(allLevelBagsWithShinyGold)))

############## SECOND PART OF PUZZLE ################
def secPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DaySeven/input.txt")

    bagRulesData = [bagRule(bagRuleLine) for bagRuleLine in readMyFile.split('\n') if bagRuleLine != '']

    res = 0
    values = []
    shinyGoldBag = next(bag for bag in bagRulesData if "shiny gold" in bag.bagName)
    

    print(findNumberOfAllLevelBagsInside(bagRulesData, shinyGoldBag, 1) - 1)
    


if __name__ == "__main__":
    firstPart()
    secPart()