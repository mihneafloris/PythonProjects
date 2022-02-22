text = "No, no, no, my brain in my head."  \
       "It will have to come out."  \
       "Out? Of my head?" \
       "Yes! All the bits of it. Nurse! Nurse! Nurse!"
s = 0
for letter in text:
    letter=letter.lower()
    if letter.islower():
        idx=ord(letter)-ord("a")
        s=s +idx**2

print(s)
