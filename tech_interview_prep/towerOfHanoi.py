# the intuition is , move (n-1) disks from start to middle,move nth disk from start to end, move (n-1) disks from middle to end.
# to get this intuition try solving for cases with n=1,2,3,4 disks, you will see th pattern.


def hanoi(n,start,end):
    if(n==1):
        pm(start,end)
    else:
        middle = 6-(start+end)
        hanoi(n-1,start,middle)
        pm(start,end)
        hanoi(n-1,middle,end)


def pm(start,end):
    print(start,'->',end)


hanoi(3,1,3)