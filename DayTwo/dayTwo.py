############### FIRST PART OF PUZZLE #################

def readfile(name):
        with open(name) as myFile:
            return myFile.read()

def firstPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayTwo/input.txt")
    fileLines = [x for x in readMyFile.split('\n') if x != '']

    sum = 0
    for line in fileLines:
        lineInfo = line.split(' ')
        if ('-' in lineInfo[0]):
            (start, end) = lineInfo[0].split('-') 
        else:
            (start, end) = (-1, -1)
        ch = lineInfo[1].replace(':','')
        passw = lineInfo[2]
        numOfChInPassw = len([x for x in passw if x == ch])

        if (int(start) <= numOfChInPassw and int(end) >= numOfChInPassw):
            sum += 1
    
    print("Result:" + str(sum))

def secPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayTwo/input.txt")
    fileLines = [x for x in readMyFile.split('\n') if x != '']

    sum = 0
    for line in fileLines:
        lineInfo = line.split(' ')
        if ('-' in lineInfo[0]):
            (start, end) = lineInfo[0].split('-') 
        else:
            (start, end) = (-1, -1)
        ch = lineInfo[1].replace(':','')
        passw = lineInfo[2]

        if ((passw[int(start) - 1] == ch or passw[int(end) - 1] == ch) and passw[int(start) - 1] != passw[int(end) - 1]):
            sum += 1
    
    print("Result:" + str(sum))

if __name__ == __name__:
    firstPart()
    secPart()