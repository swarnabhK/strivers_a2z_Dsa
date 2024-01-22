#Pattern – 3: Right-Angled Number Pyramid

"""
1
1 2 
1 2 3
"""

def pattern(n):
    for i in range(0,n):
        s= 0
        for j in range(0,i+1):
            s+=1
            print(s,end=" ")
        print()


pattern(5)