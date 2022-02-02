quarters = .25 #decimal form of each coin. 
dimes = .10
nickels = .05
pennies = .01
dollar = 1.0 # the final goal and variable tested against the user's input

print("Welcome to the change game! Type in the correct amount of coins to make a dollar \n")
inQuarters = int(input("How many quarters are you entering?: ")) #input quarters
inNickels = int(input("How many nickels are you entering?: ")) #nickels
inDimes = int(input("How many dimes are you entering?: ")) #dimes
inPennies = int(input("How many pennies are you entering?: ")) # pennies

tQuarters = quarters * inQuarters # total quarters multipling the decimal form of the coin times the amount entered
tNickels = nickels * inNickels # total nickels
tDimes = dimes * inDimes # total dimes
tPennies = pennies * inPennies #total pennies

total = tQuarters + tNickels + tDimes + tPennies #adding

if(total == dollar):
    print("Congratulations! You win the game!") # winning output
else:
    if(total > dollar):
        print("Sorry, you lost the game because your amount was ", total-dollar, " too high.") # subtracting total-dollar to get the amount over
    else:
        print("Sorry, you lost the game because your amount was ", dollar-total, " too small.") # subtracting dollar-total to get the amount under
