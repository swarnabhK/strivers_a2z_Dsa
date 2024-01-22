#Pattern – 16: Alpha-Ramp Pattern

"""
A 
B B
C C C
D D D D
E E E E E
F F F F F F
"""

def pattern(N):
    c = 65
    for i in range(N):
        for j in range(i+1):
            print(chr(c),end="")
        c+=1
        if(i!=N-1):
          print()

pattern(6)
          