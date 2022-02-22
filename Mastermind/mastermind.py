"""
Mastermind Game
4663675
Floris Mihnea
"""
#Importing tools

from mastertools import gencode, goodplace, goodcolour

while True:
    #Main program

    max_allowed=10
    attempt=0

    #Generate secret code
    code=gencode()
    print(code)
        
    attempt = 0
    max_allowed = 10

    while attempt < max_allowed:
        guess=[]
        while len(guess)<4:
            i=int(input("Enter four colours (numbers from 1 to 6): "))
            guess.append(i)
        print( "The number of correct colours in the correct place is: ",goodplace(code,guess))
        print("The number of correct colours in the wrong place is: " ,goodcolour(code,guess))
        if code==guess:
            print("You have won")
            break
        else:
            print("Enter a new guess")
            attempt+=1
    else:
        print("You have reached the maximum amount of attempts. Game over! Correct code was: " ,code)

    answer=str(input("Do you want to play again?(Y/N): "))
    if answer=="Y":
        continue
    elif answer=="N":
        print("Goodbye!")
        break
    else:
        raise ValueError("Bad input")
