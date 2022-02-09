def sumOfList(aList): ## function to sum up the list
    sum = 0 # sum will be returned
    i = 0
    for i in range(0, len(aList)): # start from 0 till the length of the list, which is the end
        sum += aList[i] # add to sum the list at i 
    return sum
def evensOfList(aList):
    evenList = [] # create empty list
    i = 0
    for i in range(0, len(aList)): # start from 0 till the length of the list, which is the end
        if (aList[i] % 2 == 0):
            evenList.append(aList[i]) # append evenList if the number is even
    return evenList # then return the list
def oddsOfList(aList):
    oddList = []
    i = 0
    for i in range(0, len(aList)): # start from 0 till the length of the list, which is the end
        if (aList[i] % 2 == 1):
            oddList.append(aList[i]) # append oddList if the number is even
    return oddList # then return the list
# listOfNumbers = [0, 68, 41, 88, 16, 40, 65, 97, 85] # just an example list 
print(sumOfList(listArr))# calling the functions , first one sum
print(evensOfList(listArr)) 
print(oddsOfList(listArr))
