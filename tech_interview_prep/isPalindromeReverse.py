def isPalindrome(string,left,right):
    if left>=right:
        return True
    if string[left]!=string[right]:
        return False
    return isPalindrome(string,left+1,right-1)


st = "racecar"
st2 = "ronnie"
print(isPalindrome(st,0,len(st)-1))
print(isPalindrome(st2,0,len(st2)-1))
