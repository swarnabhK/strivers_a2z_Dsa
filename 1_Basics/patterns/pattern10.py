#Pattern – 10: Half Diamond Star Pattern
"""
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *
"""
#half right angled triangle: total available is 12

def half_pyramid(N):
    for i in range(N):
        #left side is always N-1 spaces
        for j in range(N-1):
            print(" ",end="")
        #print the stars
        for j in range(i+1):
            print("*",end="")
        #print the remaining spaces
        for j in range(0,N-i-1):
            print(" ",end="")
        print()

def half_inverted_pyramid(N):
    for i in range(N):
        #left side is always N-1 spaces
        for j in range(N-1):
            print(" ",end="")
        #print the stars
        for j in range(0,N-i):
            print("*",end="")
        #print the remaining spaces
        for j in range(i):
            print(" ",end="")
        if(i!=N-1):
            print()
            
def pattern(N):
    half_pyramid(N)
    half_inverted_pyramid(N)

pattern(6)