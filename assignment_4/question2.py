def gatherNumbers(size):
    numbersSeries = []
    for i in range(0,size):
        userInput = float(input("Enter any integer or floating point number: "))
        numbersSeries.append(userInput)
    return numbersSeries
def lowestOfList(inputedNumbers, size):
    lowestNum = inputedNumbers[0]
    for i in range(0,size):
        if lowestNum > inputedNumbers[i]:
            lowestNum = inputedNumbers[i]
    return lowestNum
def highestOfList(inputedNumbers, size):
    highestNum = inputedNumbers[0]
    for i in range(0,size):
        if  inputedNumbers[i] > highestNum:
            highestNum = inputedNumbers[i]
    return highestNum
def totalOfList(inputedNumbers, size):
    sum = 0
    for i in range(0,size):
        sum += inputedNumbers[i]
    return sum
def averageOfList(inputedNumbers,size):
    sum = 0
    for i in range(0,size):
        sum += inputedNumbers[i]
    return sum/size


def main():
    amountNumbers = 20 # change to 20 when completed
    userNumbers = gatherNumbers(amountNumbers)
    print(userNumbers)
    print("Lowest number is " + str(lowestOfList(userNumbers, amountNumbers)))
    print("Highest number is " + str(highestOfList(userNumbers, amountNumbers)))
    print("Total is " + str(totalOfList(userNumbers, amountNumbers)))
    print("Average is " + str(averageOfList(userNumbers, amountNumbers)))
main()
