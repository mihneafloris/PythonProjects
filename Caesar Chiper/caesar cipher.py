"""
Caesar Cipher
Floris Mihnea
4663675
"""

def idxabc(ch):
    #return index in alphabet 0-25
    i= ord(ch.upper())-ord("A")
    return i

def shift(ch, ikey):
    #upper case alphabetic character
    if ch.isupper():
        newch=chr((ord(ch)+ikey%26))
        if ord(newch)>ord("Z"):
            newch= chr(ord("A")-1+ ord(newch)-ord("Z"))
    elif ch.islower():
        newch=chr((ord(ch) + ikey%26))
        if ord(newch)>ord("z"):
            newch=chr(ord("a")-1+ord(newch)-ord("z"))
    else:
        newch=ch
    return newch

def shiftlines(lines,ikey):
    #Do Caesar shift on a list of lines
    newlines=[]
    for line in lines:
        newline=""
        for ch in line:
            newch=shift(ch,ikey)
            newline=newline+newch
        newlines.append(newline)
    return newlines
        
def getfreq(lines):
    # get list with frequencies from "A" to "Z"
    # also includes lower case
    totals = 26 *[0]
    for line in lines:
        low_line=line.lower()
        #get the nummber of hits for a ch in one line
        for ch in low_line:
            if ch.isalpha():
                totals[ord(ch)-ord("a")]+=1
        #converting it to frequencies/percentages
        freqlist=[]
        nr=sum(totals)
        for total in totals:
            freq=100*total/nr
            freqlist.append(freq)
    return freqlist
#print (getfreq(text))

#getting the difference in frequency between two letters
def listdif(a,b):
    dif=0.0
    for i in range(len(a)):
        dif+=abs(a[i]-b[i])
    return dif
#minimum index function
def idxmin(lst):
    min=lst[0]
    for i in range(len(lst)):
        if lst[i]<min:
            min=lst[i]
            idx=i
    return idx
"""
endcoded=shiftlines(text,5)
decoded=shiftlines(encoded,-5)
a=getfreq(text)
b=getfreq(encoded)
c=getfreq(decoded)
print(listdif(a,b))
print(listdif(a,c))
a=[2,3,4,-1,5,6]
print(idxmin(a))
"""

f_freq=open("ch-freq-en.txt","r")
text=f_freq.readlines()
standard_f=26*[0]
#cleaning the freq list
for i in range(len(text)):
    a,b=text[i].split("\t")
    #a=letter and b=freq
    b=b.strip("\n")
    standard_f[ord(a)-ord("A")]=float(b)
#checking the frequency values
#standard_f.sort(reverse=True)
#print(standard_f)

#testing the decoding part with key=-5
test5=open("test5.txt","r")
test_text=test5.readlines()
new=shiftlines(test_text,-5)
out=open("out.txt","w" ,encoding="utf-8")
out.writelines(new)
out.close()

#for the first file -- secret 0
"""
s0=open("secret0.txt","r")
d0=open("decoded0.txt"","w",encoding="utf-8")
text=s0.readlines()
deviations[]
for key in range(26):
    new=shiftlines(text,key)
    freq=getfreq(new)
    deviations.append(listdif(freq,standard_f))
key=idxmin(deviations)
print ("Secret0 was decoded by ", key)
d0.writelines(shiftlines(text,key))
d0.close()
"""

#now everything in a loop
for i in range (8):
    #opening and reading from out files
    s=open("secret%i.txt" %i,"r")
    d=open("decoded%i.txt" %i,"w", encoding="utf-8")
    text=s.readlines()
    deviations=[]
    #finding the best key(the min deviation)
    for key in range(26):
        new=shiftlines(text,key)
        freq=getfreq(new)
        deviations.append(listdif(freq,standard_f))
    key=idxmin(deviations)

    print("Secret%i was decoded by key=" %i, key)
    d.writelines(shiftlines(text,key))
    d.close()
