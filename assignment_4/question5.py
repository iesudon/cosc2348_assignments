import statistics
def findStandardDev(numList):
    return statistics.stdev(numList)      
def findAverage(numList):
    sumOf = sum(numList)
    lengthList = len(numList)
    return sumOf/lengthList
def findMedian(numList):
    return statistics.median(numList)
def createDivisionList(numList):
    divisionList = []
    try:
        for i in range(0,len(numList)-1):
            divisionList.append((numList[i]/numList[i+1]))
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        exit()
    return divisionList
def main():
    listOfNumbers = []
    numOfNumbers = int(input("Enter the number of numbers you want to put into the list: "))
    while numOfNumbers <= 10:
        numOfNumbers = int(input("Too few, enter a value greater than ten: "))
    for i in range(0,numOfNumbers):
        userInputAtI = int(input("Enter the number you want to enter between 0 to 100: "))
        while userInputAtI < 0 or userInputAtI > 100:
            userInputAtI = int(input("The number you want to enter has to be in between 0 to 100: "))
        listOfNumbers.append(userInputAtI)
    print("The median of that list is: " + str(findMedian(listOfNumbers)))
    print("The Standard deviation of that list is: " + str(findStandardDev(listOfNumbers)))
    print("The Average of that list is: " + str(findAverage(listOfNumbers)))
    newList = createDivisionList(listOfNumbers)
    print("The new list is: " + str(newList))
main()
