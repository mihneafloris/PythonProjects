"""
Mastermind Game
4663675
Floris Mihnea
"""
#Import modules

import random

#Define functions

#Generate four random colours
def gencode():
    colour =[]
    while len(colour)<4:
        icol = random.randint(1,6)
        colour.append(icol)
    return colour

#Check for correct colour and place

def goodplace(code,guess):
    counter=0
    for x,y in zip(guess,code):
        if x==y:
            counter=counter+1
    return counter
    

def goodcolour(code, guess):
    k=0
    for i in range(len(guess)):
        for j in range (len(code)):
            if guess[i]==code[j] and code[i]!=guess[i]:
                k=k+1
    return k




















    
