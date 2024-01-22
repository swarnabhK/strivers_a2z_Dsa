#Pattern – 9: Diamond Star Pattern
"""
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *
"""

#it is a pyramid and inverted pyramid pattern

def pyramid(N):
    for i in range(N):
        #print spaces
        for j in range(0,N-i-1):
            print(" ",end="")
        #print stars
        for j in range(0,2*i+1):
            print("*",end="")
        #print spaces again
        for j in range(0,N-i-1):
            print(" ",end="")
        print()

def inverted_pyramid(N):
    for i in range(N):
        #print the spaces
        for j in range(i):
            print(" ",end="")
        #print the stars
        for j in range(0,2*N-(2*i+1)):
            print("*",end="")
        #print the spaces again
        for j in range(i):
            print(" ",end="")
        if(i!=N-1):
            print()

def pattern(N):    
  pyramid(N)
  inverted_pyramid(N)


pattern(6)