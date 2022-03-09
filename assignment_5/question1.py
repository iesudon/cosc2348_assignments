def convertAlphaToMorse(userStringAt):
    alphaToMorse = {
        ' ':"/",
        ',':"--..--",
        '.':".-.-.-",
        '?':"..--..",
        '0':"-----",
        '1':".----",
        '2':"..---",
        '3':"...--",
        '4':"....-",
        '5':".....",
        '6':"-....",
        '7':"--...",
        '8':"---..",
        '9':"----.",
        'A':".-",
        'B':"-...",
        'C':"-.-.",
        'D':"-..",
        'E':".",
        'F':"..-.",
        'G':"--.",
        'H':"....",
        'I':"..",
        'J':".---",
        'K':"-.-",
        'L':".-..",
        'M':"--",
        'N':"-.",
        'O':"---",
        'P':".--.",
        'Q':"--.-",
        'R':".-.",
        'S':"...",
        'T':"-",
        'U':"..-",
        'V':"...-",
        'W':"-..-",
        'Y':"-.--",
        'Z':"--.."
    }
    toUpperUserStr = userStringAt.upper()
    return alphaToMorse[toUpperUserStr]
def main():
    userString = input("Enter the string you want to convert to morse code: \n")
    newString = ""
    for i in range(0,len(userString)):
        newString += convertAlphaToMorse(userString[i])
        newString += ' '
    print(newString)
main()
