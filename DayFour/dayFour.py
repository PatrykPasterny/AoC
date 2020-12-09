import re

class Validator: 
    validEyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
    def validateInterval(self, number, start, end):
        return number >= start and number <= end
    
    def validateYear(self, year):
        return re.match(r"^[0-9]{4}$", str(year))
      
    def validateHeight(self, height):
        resultPart = re.match(r"^[0-9]+(cm|in)$", str(height)) 
        if resultPart and str(height).endswith("cm"):
            return resultPart and self.validateInterval(int(str(height)[:-2]), 150, 193)
        else:
            return resultPart and self.validateInterval(int(str(height)[:-2]), 59, 76)
    
    def validateHexColor(self, color):
        return re.match(r"^#([0-9]|[a-f]){6}$", str(color))

    def validateEyeColor(self, color):
        return color in self.validEyeColor
    
    def validatePassportId(self, id):
        return re.match(r"^[0-9]{9}$", str(id))

    

############### FIRST PART OF PUZZLE #################

def readfile(name):
        with open(name) as myFile:
            return myFile.read()

def firstPart():
    labelsToValidate = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    optionalLabel = 'cid'
    readMyFile = readfile("C:/Users/admin/Desktop/MyImportant/AOC/DayFour/input.txt")

    passportsData = readMyFile.split('\n\n')
    passports = []
    for passportData in passportsData:
        passportData = passportData.replace('\n', ' ')
        passport = {}
        for singleInfo in passportData.split(' '):
            if (singleInfo == ''):
                continue

            (sInputId, sInput) = singleInfo.split(':')
            passport[sInputId] = sInput

        passports.append(passport)
    
    sum = 0
    validPassports = []
    for passport in passports:
        validatedVariables = [x for x in passport.keys() if x in labelsToValidate]
        if len(validatedVariables) == 8:
            validPassports.append(passport)
            sum += 1
        elif len(validatedVariables) == 7 and optionalLabel not in validatedVariables:
            validPassports.append(passport)
            sum += 1
        
    print(sum)
    return validPassports
   
############## SECOND PART OF THE PUZZLE #################
def secPart():
    validator = Validator()
    validPassports = []
    passports = firstPart()
    for passport in passports:
        isPassportValid = False
        for key in passport.keys():
            valueToValidate = passport[key]
            if 'byr' in key:
                isPassportValid = validator.validateYear(valueToValidate) and validator.validateInterval(int(valueToValidate), 1920, 2002)
            elif 'iyr' in key:
                isPassportValid = validator.validateYear(valueToValidate) and validator.validateInterval(int(valueToValidate), 2010, 2020)
            elif 'eyr' in key:
                isPassportValid = validator.validateYear(valueToValidate) and validator.validateInterval(int(valueToValidate), 2020, 2030)
            elif 'hgt' in key:
                isPassportValid = validator.validateHeight(valueToValidate)
            elif 'hcl' in key:
                isPassportValid = validator.validateHexColor(valueToValidate)
            elif 'ecl' in key:
                isPassportValid = validator.validateEyeColor(valueToValidate)
            elif 'pid' in key:
                isPassportValid = validator.validatePassportId(valueToValidate)
            else:
                isPassportValid = True
            
            if not isPassportValid:
                break

        if isPassportValid:
            validPassports.append(passport)
    
    print(len(validPassports))
            
if __name__ == "__main__":
    firstPart()
    secPart()