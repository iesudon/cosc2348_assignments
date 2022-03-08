def createDictionarySeries(size):
    seriesDictionary = {}
    for i in range(1,size):
        seriesDictionary[i] = i*i
    return seriesDictionary
def main():
    sizeOfDictionary = int(input("Enter a number to create a dictionary in the range bewteen one and that number: "))
    userDict = createDictionarySeries(sizeOfDictionary)
    print("Your Dictionary: \n")
    print(userDict)
main()
