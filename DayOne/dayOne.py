############### FIRST PART OF PUZZLE #################

def readfile(name):
        with open(name) as myFile:
            return myFile.read()

def firstPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayOne/input.txt")
    nums = [int(x) for x in readMyFile.split('\n') if x.isnumeric()]

    tempNums = nums[:]
    for num in nums:
        tempNums.remove(num)
        for num2 in tempNums:
            if (num + num2) == 2020:
                print("1:" + str(num) + " " + "2:" + str(num2)) 
                print("Result: " + str(num * num2))

############## SECOND PART OF PUZZLE ########################

def secPart():
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayOne/input.txt")
    nums = [int(x) for x in readMyFile.split('\n') if x.isnumeric()]

    tempNums1 = nums[:]
    for num in nums:
        tempNums1.remove(num)
        tempNums2 = tempNums1[:]
        for num1 in tempNums1:
            tempNums2.remove(num1)
            for num2 in tempNums2:
                if (num + num1 + num2) == 2020:
                    print("1:" + str(num) + " " + " 2: " + str(num1) + " 3: " + str(num2)) 
                    print("Result: " + str(num * num1 * num2))


if __name__ == "__main__":
    firstPart()
    secPart()
    print("Done")


