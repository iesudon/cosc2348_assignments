userVal = float(input("What is your age in years in decimal notation?: ")) # asking the user what their age is in decimal notation, 
# and passing to if statements as float
if(userVal <= 1): #infant statement, if they are one years old or younger
  print("You are an infant!") 
elif(userVal > 1 and userVal < 13): # child statement, if they are older than one and younger than 13
  print("You are a child!")
elif(userVal >= 13 and userVal < 20): # teenager statement, if they are at least 13 or younger than 20
  print("You are a teenager!")
else: # if the user is older than this, the if statement will go to this
  print("You are an adult!")
