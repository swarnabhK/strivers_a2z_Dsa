#Pattern-5: Inverted Right Pyramid

"""
* * *
* * 
*
"""
#00,01,02 10,11, 20 i=0,j=2, i=1,j=1,i=2,j=0 (n-i)

def pattern(n):
    for i in range(n):
        for j in range(0,n-i):
            print("*",end = " ")
        print()


pattern(4)