#Pattern – 4: Right-Angled Number Pyramid – II
"""
1
2 2 
3 3 3
"""

def pattern(n):
    for i in range(n):
        for j in range(0,i+1):
            print(i+1,end=" ")
        print()

pattern(4)
            