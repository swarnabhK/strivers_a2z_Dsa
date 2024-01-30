#According to rule from left to right the roman number should contain largest to smallest, in case there is a smaller number before a larger number,
# The value of the smaller number is subtracted from the current sum.
def roman_to_integer(s):
    num = 0
    values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(s)-1):
        if(values[s[i]]<values[s[i+1]]):
            num = num-values[s[i]]
        else:
            num = num+values[s[i]]
    #in the loop we haven't taken care of the case : last roman literal.
    num = num+values[s[len(s)-1]]
    return num


print(roman_to_integer('III')) #3
print(roman_to_integer('LVIII')) #58
print(roman_to_integer('MCMXCIV')) #1994
