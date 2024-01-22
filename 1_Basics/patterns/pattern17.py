#pattern 17: Alpha-Hill Pattern
"""
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA
"""
#no of chars each line 11(2*N-1), left side, right side starts with -1 of where left side ends, 5 sp 1 c 5 sp, 4 sp 3 ch 4 sp, no of spaces, 10,8,6,4,2,0 n-i-1

def pattern(N):
    for i in range(N):
        c = 64
        #spaces left
        for _ in range(0,N-i-1):
            print(" ",end="")
        for _ in range(i+1):
            c+=1
            print(chr(c),end="")
        for _ in range(i):
            c-=1
            print(chr(c),end="")
        for _ in range(0,N-i-1):
            print(" ",end="")
        if(i!=N-1):
          print()

pattern(6)