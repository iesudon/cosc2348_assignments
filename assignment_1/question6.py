userInput = int(input("What year are you checking for?: ")) # getting user input
if(userInput % 100 == 0): # checking divisible by 100 case
    if(userInput % 400 == 0): # checking for if it is also divisible by 400
        print(userInput, " is a leap year.")
    else: ## if it isn't, then the year is not a leap year
        print(userInput, " is not a leap year.")
else: ## two things can happen here
    if(userInput % 4 == 0): ## either it is a leap year because it is divisible by 4
        print(userInput, " is a leap year.")
    else:
        print(userInput, " is not a leap year.") # or it isn't
