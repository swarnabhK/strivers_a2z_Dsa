#Pattern – 13: Increasing Number Triangle Pattern
"""
1
2  3
4  5  6
7  8  9  10
11  12  13  14  15
16  17  18  19  20  21
"""
# 0 -1, 1->2. inner loop dependent on i+1

def pattern(N):
     s=0
     for i in range(N):
          for j in range(i+1):
              s+=1
              print(s,end=" ")
          print()


pattern(6) 