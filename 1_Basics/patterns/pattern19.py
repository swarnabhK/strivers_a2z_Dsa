#Pattern-19: Symmetric-Void Pattern

"""
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************
"""

def upper_pattern(N):
    for i in range(N):
        for _ in range(N-i):
            print("*",end="")
        
        for _ in range(2*i):
            print(" ",end="")
        
        for _ in range(N-i):
            print("*",end="")
        print()

def lower_pattern(N):
    for i in range(N):
        for _ in range(i+1):
            print("*",end="")
        for _ in range(2*(N-(i+1))):
            print(" ",end="")
        for _ in range(i+1):
            print("*",end="")
        if(i!=N-1):
            print()

def pattern(N):
    upper_pattern(N)
    lower_pattern(N)

pattern(6)