# numerical integration
# diagrams and modelling

from random import randint
print("*** 24 game ***")
print()
print("Try to make an expresion which results in a number as close to 24 as possible")
print("Use all numbers only once")
#geenrate 4 one-digit numbers
digits = []
for i in range(4):
    digits.append(randint(1,9))
    if i <3:
        print(digits[-1], end=",")
    else:
        print(digits[-1])

    
#user enters solution
answer = input("Enter your solution (e.g. (2+2)*(1+5): ")
answer = answer+" "
#check validity of the solution
invalid = False
for i in range(len(answer)):
    if answer[i].isdigit():
        #Symbols before and afters should not be digits
        if answer[i-1].isdigit() or answer[i+1].isdigit():
            invalid = True
        else:
            #remove digit d from list of digits
            d = int(answer[i])
            if d in digits:
                digits.remove(d)
            else:
                invalid = True
    else:
        if not answer[i] in "+-*/ ()":
            print(answer[i])
            invalid = True

#All numbers used?
if len(digits) >0:
    invalid = True 

#Print invalid
if not invalid:      
    #What is the value of the answer:
    x = eval(answer)
    if x == 24:
        print ("Well done")
    else:
        print("Answer gives:",x,"which is", abs(24-x),"away from 24")
else:
    #Print message
    print("You made a mistake of using not all digits once")
