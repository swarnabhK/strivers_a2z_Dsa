#right angled triangle pattern

"""
* 
* * 
* * *
"""

#ist iteration-1 , 2nd iteration-2 , 3rd iteration-3

def pattern(n):
    for i in range(n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()

pattern(4)