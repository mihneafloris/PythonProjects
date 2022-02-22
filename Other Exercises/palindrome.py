def isPalindrome(num):
    return str(num) == str(num)[::-1]
def fn(n):
    max_palindrome=1
    for x in range (n, 1, -1):
        for y in range (n, x-1, -1):
            if isPalindrome(x*y)and x*y>max_palindrome:
                max_palindrome=x*y
            
    return max_palindrome

print (fn(999))


i=0
for i in range(0,20,1):
    print (i)

