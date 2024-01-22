#find sum of first N numbers using recursion

def sum_N(N,s):
    if(N==0):
        return s
    s+=N
    return sum_N(N-1,s)

def sum_func(N):
    if(N==0):
        return 0
    return N+sum_func(N-1)

print(sum_N(10,0))

print(sum_func(10))