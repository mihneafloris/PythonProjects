from random import randint,seed
import numpy as np

def fillhall(seedno, npeople):
    seed(seedno)
    return[randint(2,13) for i in range(npeople)]
waiting = fillhall(6,100)

numberofpeople = 100
waiting = fillhall(6,numberofpeople)

numberremaining = numberofpeople
i=0
T=0
while numberremaining >0:
    takenaboard = waiting[i*9:min((i+1)*9,numberofpeople)]
    nf = np.size(np.unique(np.array(takenaboard)))
    fmax=max(takenaboard)
    T=T+7 +(2.3+2.0)*fmax +5*nf
    numberremaining = numberremaining -9
    i=i+1
print(T)
