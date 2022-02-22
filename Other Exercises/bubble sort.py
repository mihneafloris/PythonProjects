lst = [5,1,8,4,5,9,9,2,5,67,53,12]
swapping = True
while swapping:
    
    #optimistic: assume we're done
    swapping = False
    #Do a sorting run
    for i in range(len(lst)-1):
        #Values in the wrong order?
        if lst[i] > lst[i+1]:
            save     = lst[i]
            lst[i]   = lst[i+1]
            lst[i+1] = save
            swapping = True

print("Sorted list",lst)
