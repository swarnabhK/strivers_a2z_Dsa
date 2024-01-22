#Pattern – 7: Star Pyramid
"""
     *     
    ***    
   *****   
  *******  
 ********* 
***********
"""
def pattern(N):
    for i in range(0,N):
        for j in range(0,N-i-1):
            print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        for j in range(0,N-i-1):
            print(" ",end="")
        print()


pattern(6)