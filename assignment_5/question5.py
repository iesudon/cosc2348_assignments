import string
def firstToUpperCase(userStr):
    newStr = userStr.title()
    return newStr
def removeSpaces(userStr):
    newStr = ""
    for i in range(0,len(userStr)):
        newStr += userStr[i].strip()
    return newStr
def addSpacesAndDollarSigns(userStr):
    newStr = ""
    for i in range(0,len(userStr)):
        if i > 1 and userStr[i].isupper():
            newStr += " "
        if userStr[i] == "s" or userStr[i] == "S":
            newStr += "$"
        else:
            newStr += userStr[i]
    return newStr
def removeDollarSigns(userStr):
    newStr = ""
    for i in range(0,len(userStr)):
        if userStr[i] == "$":
            newStr += "s"
        else:
            newStr += userStr[i]
    return newStr
def main():
    userStr = "this is the string for the class"
    print(userStr)
    userStr = firstToUpperCase(userStr)
    print(userStr)
    userStr = removeSpaces(userStr)
    print(userStr)
    userStr = addSpacesAndDollarSigns(userStr)
    print(userStr)
    userStr = removeDollarSigns(userStr)
    print(userStr)
main()
