#Pattern-15: Reverse Letter Triangle Pattern

"""
A B C D E F
A B C D E 
A B C D
A B C
A B
A
"""

def pattern(N):
    for i in range(N):
        c = 65
        for j in range(0,N-i):
            print(chr(c),end=" ")
            c+=1
        if(i!=N-1):
          print()

pattern(6)