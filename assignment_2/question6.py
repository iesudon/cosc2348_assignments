def factorial(n): #factorial function
    temp = n # temp will store the initial value 
    for i in range (1, n): # run through each number 1 through n
        temp *= i # add the multiple of i and temp repeatidly
    return temp
def starsForwardsAndBack():
    x = 0
    for x in range(0,6): #print * 6 times, stepping forwards
        print('*'*x) # print * x amount of times
    x = 0
    for x in reversed(range(0,6)): #print * 6 times, backwards
        print('*'*x) # print * x amount of times
def factorialMathFunction(): #factorial function
    numN = int(input("Type in the n value: ")) ## take the input from the user for n
    numR = int(input("Type in the r value: ")) ## and r
    numerator1 = (factorial(numN))
    denominator1 = ((factorial(numR)*factorial(numN-numR))) 
    numerator2 = (factorial(numN))
    denominator2 = (factorial(numN-numR))
    print (numerator1/denominator1)
    print (numerator2/denominator2)
def selectionSort(arr, size):
    i = 0
    for i in range(0, size-1): ## for int i in range 0, till size-1
        unsortedMin = i ## the min value of the list is i
        j = i + 1 # j, another variable is i + 1
        while (j < size): # while  j is less than size
            if arr[j] < arr[unsortedMin]: # and if arr[j] is smaller than arr at min
                unsortedMin = j # min is now equal to j
            j = j + 1 # add one to j
        temp = arr[i] # temporary variable is equal to arr at i
        arr[i] = arr[unsortedMin] ## arr at i is equal to arr at unsortedMin
        arr[unsortedMin] = temp ## arr at unsorted min is equal to temp
## example list,  use any that is named listArr = [0, 68, 41, 88, 16, 40, 65, 97, 85]
starsForwardsAndBack() ## call each function
factorialMathFunction() ## call factorialMathFunction, which will also call factorial
# print (listArr) ## print unsorted List
# selectionSort(listArr, len(listArr))
# print (listArr)
