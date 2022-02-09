def starsForwards():
    x = 0
    for x in range(0,6): #print * 6 times, stepping forwards
        print('*'*x) # print * x amount of times
def starsBackwards():
    x = 0
    for x in reversed(range(0,6)): #print * 6 times, stepping backwards
        print('*'*x) # print * x amount of times
starsForwards() #function call for forwards
starsBackwards() #function call for backwards
