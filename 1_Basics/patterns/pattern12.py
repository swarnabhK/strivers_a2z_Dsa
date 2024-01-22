"""
1          1
12        21
12       321
1234    4321
12345  54321
123456654321
"""

#number+no of spaces+ number, 1 10 spaces 1, 2numbers 8 spaces 2 numbers, 3 numbers 6 spaces 3 numbers
#10,8,6,4,2,0
#2n-(2*i+2) no of spaces

def pattern(N):
    for i in range(N):
        s=0
        #print the initial numbers
        for j in range(i+1):
            s+=1
            print(s,end="")
        #print the spaces
        for j in range(0,2*(N-(i+1))):
            print(" ",end="")
        #print the next numbers
        for j in range(i+1):
            print(s,end="")
            s-=1
        print()

pattern(6)