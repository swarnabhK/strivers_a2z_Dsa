#Pattern – 11: Binary Number Triangle Pattern

"""
1
01
101
0101
10101
010101
"""
def pattern(N):
    #start with a true bit at the level
    for i in range(N):
        if(i%2==0):
            bit = True
        else:
            bit = False      
        for j in range(0,i+1):
            if(bit==True):
                print("1",end="")
            else:
                print("0",end="")
            bit=not bit
        if(i!=N-1):
          print()

pattern(6)