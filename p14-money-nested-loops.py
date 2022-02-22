# Simple approach: nested for-loops
# Order of for-loopa is important, m has to be low so start with m!

for m in range(1,10):# From 4/5 digit it is clear that m is 1 (and s is 8 or 9)
    for e in range(10):
        for n in range(10):
             for d in range(10):
                for s in range(1,10):
                     for o in range(10):
                         for r in range(10):
                             for y in range(10):
                                 # Use set for test of each digit only once
                                 lst = list(set([s,e,n,d,m,o,r,y]))
                                 if len(lst)==8:

                                    send = s*1000+e*100+n*10+d
                                    more = m*1000+o*100+r*10+e
                                    money = m*10000+o*1000+n*100+e*10+y
                                    if send+more==money:
                                        print(send,"+",more,"=",money)
