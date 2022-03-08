import random

def generateList(size):
    list = []
    for i in range(0,size):
        list.append(random.randint(0, 20))
    return list

def secondHighestOfList(listOfNumbers, size):
    largestNum = listOfNumbers[0]
    secondHighestNum = listOfNumbers[0]
    for i in range(0,size):
        if listOfNumbers[i] > largestNum:
            largestNum = listOfNumbers[i]
    for i in range(0,size):
        if listOfNumbers[i] > secondHighestNum and listOfNumbers[i] != largestNum:
            secondHighestNum = listOfNumbers[i]
    return secondHighestNum

def removeRepeatingNumbers(listOfNumbers,size):
    workingComparisonList = []
    for i in range(0,size):
        if listOfNumbers[i] not in workingComparisonList:
            workingComparisonList.append(listOfNumbers[i])
    return workingComparisonList

def main():
    size = 100
    list = generateList(size)
    print("Original list: " + str(list))
    newList = removeRepeatingNumbers(list,100)
    print("New list: " + str(newList))
    print(secondHighestOfList(list, size))
    
main()
