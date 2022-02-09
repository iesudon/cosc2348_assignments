def findAllPrimes(start, end): #function with defined start and end
    for num in range(start, end + 1): ## for a int called num in range from the start to the end plus 1
        if num > 1: # if num is greater than 1(since all prime numbers are greater than 1)
            for i in range(2, num+1): # and for i in a range of 2 till num plus 1
                if(num == 2): ## if num is two print two
                    print(num)
                    break ## break the if statement so there aren't extra prints and incorrect numbers
                elif (num % i) == 0: ## if num modulus i is 0, 
                    break # skip
                else:
                    print(num) ## if not, print num 
                    break ## then break to prevent extra prints
findAllPrimes(2,50)
            
