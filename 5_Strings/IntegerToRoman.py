#We need to apply a greedy approach, for example if we have a number 478, find the largest number just less than 478,which is 400.
# 478/400 = 1 times CD. New number is 78. 78/50: 1 times L. New number 28/10: 2 times X, New number 8/5: 1 time V, New number 3/1: 3 times I.
# That's the intuition. Go over the keys from bigger to smaller to find which key will be the largest key just smaller than the number.

def intToRoman(num):
    values = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
    roman = []
    for key,value in values.items():
        if num==0:
            break
        times = num//key
        num = num%key
        roman.append(times*value)
    return "".join(roman)


print(intToRoman(3))
print(intToRoman(58))
print(intToRoman(1994))