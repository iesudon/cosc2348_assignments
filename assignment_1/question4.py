userVal = int(input("What is your age in years?: "))
if(userVal <= 1):
  print("You are an infant!")
else if(userVal > 1 && userVal < 13):
  print("You are a child!")
else if(userVal >= 13 && userVal < 20):
  print("You are a teenager!")
else:
  print("You are an adult!")
