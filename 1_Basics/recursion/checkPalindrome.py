#check if a string is a palindrome using recursion

def check_palindrome(s,start,end):
    if(start>=end):
        return True
    if(s[start]!=s[end]):
        return False
    return check_palindrome(s,start+1,end-1)

s = "racecar"
print(check_palindrome(s,0,len(s)-1))

#approach 2 without using start and end parameters
def check_palindrome2(s):
    if(len(s)==1):
        return True
    if(s[0]!=s[-1]):
        return False
    return check_palindrome2(s[1:-1])

s = "racecar"
print(check_palindrome2(s))
s = "akjkla"
print(check_palindrome2(s))