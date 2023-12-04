#random number for each die and for the computer's number

import random            

die1 = random.randint(1,6);
die2 = random.randint(1,6);
diceValue = die1 + die2;

# need input

number = input("Please choose a number between 1 and 12: ")
computerNumber = random.randint(1,10)
print ("The computer number is: " + str(computerNumber))
print ("The result is: " + str(diceValue))

def diceDecision():
    if (diceValue == number):
        result1 = "Congrats, you won!"
        return result1
    elif (diceValue == computerNumber):
        result2 = "You lost!"
        return result2
    else:
        result3 = "It is a tie!"
        return result3
    
result = main()
print(result)