def readfile(name):
        with open(name) as myFile:
            return myFile.read()

readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayOne/input.txt")
nums = [int(x) for x in readMyFile.split('\n') if x.isnumeric()]

tempNums = nums[:]
for num in nums:
    tempNums.remove(num)
    for num2 in tempNums:
        if (num + num2) == 2020:
            print("1:" + str(num) + " " + "2:" + str(num2)) 
            print("Result: " + str(num * num2))
