def vowelsCounter(userString):
    userStringToLower = userString.lower()
    list = ["a","e","i","o","u"]
    vowelCount = 0
    for letterAt in userStringToLower:
        if letterAt in list:
            vowelCount += 1
    return vowelCount    
def constCounter(userString):
    userStringToLower = userString.lower()
    list = ["a","e","i","o","u"]
    constCount = 0
    for letterAt in userStringToLower:
        if letterAt not in list and letterAt.isspace() == False:
            constCount += 1
    return constCount 
def main():
    userInputString = input("Enter the string you want to test: ")
    print("Your string has " + str(vowelsCounter(userInputString)) + " vowels")
    print("Your string has " + str(constCounter(userInputString)) + " consonants")
main()