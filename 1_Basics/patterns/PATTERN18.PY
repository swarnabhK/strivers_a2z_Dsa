#Pattern-18: Alpha-Triangle Pattern

"""
F
E F
D E F
C D E F
B C D E F
A B C D E F
"""

#AT EACH LEVEL THE STARTING C VALUE WILL BE 65+N-i-1

def pattern(N):
    for i in range(N):
        c = 65+N-i-1
        for _ in range(i+1):
            print(chr(c),end="")
            c+=1
        if(i!=N-1):
          print()

pattern(6)