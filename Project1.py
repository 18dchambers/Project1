import math
secretNumber = 0
computerGuess = 50
low = 1
high = 100
guessCorrect = False
higher = False
invalid = True

def findMedian():
    global low, high
    
    if computerGuess == 2:
        return 1
    
    else:
        return math.ceil((int(low)+int(high)) / 2)
    
    
    
def changeRange(higher):
    global low, high
    
    
    if higher == True:
        low = computerGuess
    
    elif higher == False:
        high = computerGuess
        
secretNumber = int(input("Type a secret number between 1 and 100"))
        
if (secretNumber > 100 or secretNumber < 1):
    print("Invalid Number")

else:
    while (guessCorrect == False):
        print(computerGuess)
        tempVariable = input("Is this the correct number?")
    
        if tempVariable == "y":
            guessCorrect = True
            print("Well, it looks like I'm correct!")

        
        elif tempVariable == "n":
            guessCorrect = False
            highLow = input("Is it higher or lower?")
                            
            if highLow == "higher":
                higher = True
                            
            elif highLow == "lower":
                higher = False
                
            else:
                highLow = input("Is it higher or lower?")
                
        changeRange(higher)
        
        computerGuess = findMedian()
