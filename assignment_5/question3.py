import string

def countCharacters(userStr):
    return len(userStr)
def removeSpecialsAndPunct(userStr):
    newStr = ""
    for i in range(0,len(userStr)):
        if userStr[i] not in string.punctuation:
            newStr += userStr[i]
    return newStr
def replaceDashWithSpace(userStr):
    newStr = ""
    for i in range(0, len(userStr)):
        if userStr[i] == '-':
            newStr += ' '
        else:
            newStr += userStr[i]
    return newStr
def removeConsts(userStr):
    newStr = ""
    list = ["a","e","i","o","u"]
    constCount = 0
    for i in range(0, len(userStr)):
        if userStr[i] not in list:
            newStr += userStr[i]
    return newStr 
def main():
    str1 = "P@#yn26at^&i5ve"
    print("Symbols, Digits, and Symbols: " + str(countCharacters(str1)))
    str1 = "/*Jon is@developer & musician"
    print("Original string: "+ str1)
    print("New String without special or punctuation characters: "+removeSpecialsAndPunct(str1))
    str1 = "Emma-is-a-data-scientist"
    print("Original string: "+ str1)
    print("New String without dashes: "+ replaceDashWithSpace(str1))
    str1 = "Hello, have a good day"
    print("Original string: "+ str1)
    print("New String without consonants: "+ removeConsts(str1))
main()