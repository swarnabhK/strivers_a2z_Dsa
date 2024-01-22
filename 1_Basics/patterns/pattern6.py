#Pattern – 6: Inverted Numbered Right Pyramid
"""
1 2 3
1 2
1
"""

def pattern(n):
    for i in range(n):
        s=0
        for j in range(0,n-i):
            s+=1
            print(s,end=" ")
        print()

pattern(4)