import re

def readfile(name):
        with open(name) as myFile:
            return myFile.read()

############### FIRST PART OF PUZZLE #################

def firstPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DaySix/input.txt")

    groupsData = [[person for person in group.split('\n')] for group in readMyFile.split('\n\n') if group != '']
    groupsYesAnswers = []
    for group in groupsData:
        groupYesAnswers = set()
        for person in group:
            if re.match(r"^[a-z]+$", person.lower()):
                for answer in person:
                    groupYesAnswers.add(answer)

        groupsYesAnswers.append(len(groupYesAnswers))  

    print(sum(groupsYesAnswers))         

def secPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DaySix/input.txt")

    groupsData = [group for group in readMyFile.split('\n\n') if group != '']
    groupsAllYesAnswers = []
    for group in groupsData:
        if group.startswith('\n') and group.endswith('\n'):
            peopleInGroup = group.count('\n') - 1
        elif group.startswith('\n') or group.endswith('\n'):
            peopleInGroup = group.count('\n')
        else:
            peopleInGroup = group.count('\n') + 1
            
        groupAllYesAnswers = set()
        for answer in group.replace('\n',''):
            if group.count(answer) == peopleInGroup:
                groupAllYesAnswers.add(answer)
        
        groupsAllYesAnswers.append(len(groupAllYesAnswers))
    
    print(sum(groupsAllYesAnswers))
            
if __name__ == "__main__":
    firstPart()
    secPart()