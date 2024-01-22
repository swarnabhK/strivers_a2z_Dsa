#pattern 14: Increasing Letter Triangle Pattern

"""
A
A B
A B C
A B C D
A B C D E
A B C D E F
"""
def pattern(N):
    for i in range(N):
        c = 65
        for j in range(i+1):
            print(chr(c),end=" ")
            c+=1
        print()

pattern(6)