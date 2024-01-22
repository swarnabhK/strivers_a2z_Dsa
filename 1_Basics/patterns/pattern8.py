#Pattern – 8: Inverted Star Pyramid

"""
***********
 *********
  *******
   ***** 
    ***    
     *
"""

def pattern(n):
    for i in range(n):
        #print spaces
        for j in range(0,i):
            print(" ",end="")
        for j in range(0,2*n-(2*i+1)):
            print("*",end = "")
        for j in range(0,i):
            print(" ",end="")
        if(i!=n-1):
          print()
pattern(6)