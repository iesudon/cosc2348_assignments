def factorial(n): #factorial function
    temp = n # temp will store the initial value 
    for i in range (1, n): # run through each number 1 through n
        temp *= i # add the multiple of i and temp repeatidly
    return temp
numN = int(input("Type in the n value: ")) ## take the input from the user for n
numR = int(input("Type in the r value: ")) ## and r
numerator1 = (factorial(numN)) ## seperate values for the numerator and denominator
denominator1 = ((factorial(numR)*factorial(numN-numR)))

numerator2 = (factorial(numN))
denominator2 = (factorial(numN-numR))
print (numerator1/denominator1) ## print out the product
print (numerator2/denominator2)
