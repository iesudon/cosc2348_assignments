import random
import string


BLACKCARDS=['s','c']
REDCARDS=['h','d'] #constant values of the colors of each cards
NUMDECKS=random.randint(3,8)
MAXCARDS=52*NUMDECKS
BLACKJACK=21
MAXPLAYERS=3
DEALERS=1
NUMROUNDS=random.randint(1,10)

class Player():
    def __init__(self):
        self.__out = False
        self.__zeroCounter = 0
        self.resetAttrs()
        self.__bank = random.randint(500, 5000)
    def resetAttrs(self):
        self.__score = 0
        self.__standFlag = False
        self.__bustFlag = False
        self.__blackJackFlag = False
        self.__currentBet = 0
        self.__hand = []
    def setHand(self,card):
        self.__hand.append(card)
    def getHand(self): #dealer class
        return self.__hand
    #returns current hand
    def placeBet(self, bet):
        if(bet == 0):
            self.__zeroCounter += 1
            if(self.__zeroCounter == 3):
                self.drop()
        self.__currentBet = bet
    def doubleDown(self):
        self.__currentBet *= 2
        self.setStand()
    def setLostBet(self):
        self.__bank -= self.getBet()
    def regularWin(self):
        self.__bank += self.getBet()
    def blackJack(self):
        self.__blackJackFlag = True
        self.__bank += 2*self.getBet()
    def getScore(self):
        return self.__score
    def getStand(self):
        return self.__standFlag
    def setStand(self):
        self.__standFlag = True
    def getBust(self):
        return self.__bustFlag
    def setBust(self):
        self.__bustFlag = True
        self.lostBet()
    def getBlackJack(self):
        return self.__blackJackFlag
    def getBalance(self):
        return self.__bank
    def getBet(self):
        return self.__currentBet
    def setDrop(self):
        self.__dropFlag = True
    def getDropped(self):
        return self.__dropFlag
class Dealer():
    #initializing shoe
    def __init__(self,shoe):
        self.hand = []
        self.resetattrs()
    #initializing dealers cards, score and bust flag
    def resetattrs(self):
        self.hand = []
        self.__score = 0
        self.__bustFlag = False
    def setHand(self,card):
        self.__hand.append(card)
    def getHand(self): #dealer class
        return self.__hand

def createDeck(): #The deck creator, shoe class
    deck=['sa','s2','s3','s4','s5','s6','s7','s8','s9','s1','sj','sq','sk', 
            'ha','h2','h3','h4','h5','h6','h7','h8','h9','h1','hj','hq','hk',
                'ca','c2','c3','c4','c5','c6','c7','c8','c9','c1','cj','cq','ck',
                'da','d2','d3','d4','d5','d6','d7','d8','d9','d1','dj','dq','dk']
    return deck
def cardValuer(hand, cardN ,currentGame): #shoe class
    if(hand[cardN][1]=='a'): #if this returns 0, it will prompt the user to choose either 1 or 11
        if(currentGame > 1):
            value = int(input("Enter either 1 or 11"))
            while (value != 1 or value != 11):
                value = int(input("Enter either 1 or 11"))
            return value
        else:
            return 1
    elif(hand[cardN][1]!='a' and hand[cardN][1].isalpha() or hand[cardN][1]=='1'): #this is last incase it tries to make the ace equal to 1 or 11
        return 10
    else:
        return int(hand[cardN][1])
def createShoe(): #shoe class
    shoe=[]
    for i in range(0,NUMDECKS):
        shoe.append(createDeck())
    shuffleDecks(shoe)
    return shoe
def shuffleDecks(shoe): #dealer class
    for decks in range(0,NUMDECKS):
        random.shuffle(shoe[decks]) #shuffle each deck
    random.shuffle(shoe) #shuffle the shoe
    return shoe
def returnValue(playerCardsV): #player class
    sumOfCards=0
    for cards in range(0,len(playerCardsV)):
        sumOfCards+=cardValuer(playerCardsV[cards])
    return sumOfCards
def checkWin(playerCardsW): #dealer class
    playerValue = returnValue(playerCardsW)
    if(playerValue > 21):
        return 0
    if(playerValue == 21):
        return 2
    else:
        return 1
def handNamer(handD, currentGame): #deck class
    cardName = ""
    for i in range(0,len(handD)):
        if(handD[i][0] == "s"):
            cardName += "Spades "
        if(handD[i][0] == "h"):
            cardName += "Hearts " 
        if(handD[i][0] == "c"):
            cardName += "Clubs "
        if(handD[i][0] == "d"):
            cardName += "Diamonds "
        if(handD[i][1] == 'a'):
            cardName += "Ace"
        elif(handD[i][1] == 'k'):
            cardName += "King"
        elif(handD[i][1] == 'q'):
            cardName += "Queen"
        elif(handD[i][1] == 'j'):
            cardName += "Jack"
        else:
            cardName += str(cardValuer(handD,i,currentGame))
    return cardName
        
def setPlayers(shoe,currentCard, currentDeck):
    tempPlayers = []
    for i in range(0,3):
        tempPlayers.append(Player())
        tempPlayers[i].setHand(shoe[currentDeck][currentCard])
        currentCard+=1
    return tempPlayers

def main():
    shoe=createShoe()
    dealer = Dealer(shoe)
    tableFlag = True
    currentDeck = 0
    currentCard = 0
    currentGame = 1
    while tableFlag == True:
        print ("There are three players at this table")
        for i in range (0,3):
            players = setPlayers(shoe,currentCard,currentDeck)
            print("Player " + str(i+1) + ": \n" + str(handNamer(players[i].getHand(),currentGame)) 
                  + " Value:" + str(cardValuer(players[i].getHand(),0,currentGame)))
            while gameFlag == true:
                while roundFlag == true and roundCount >=1:
                    
        tableFlag = False
        if (currentCard%52==0):
            currentDeck+=1
        if (currentCard == MAXCARDS and currentDeck == 3):
            shoe=createShoe()            
main()
