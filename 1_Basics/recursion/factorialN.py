# 3!=3*fact(2)


#parametrised recursion
def fact(N,prod):
    if(N==1):
        return prod
    prod*=N
    return fact(N-1,prod)

print(fact(4,1))
print(fact(5,1))

#functional recursion
#fact(n) = n*fact(n-1)

def fact_func(N):
    if(N==0):
        return 1
    return N*fact_func(N-1)

print(fact_func(5))

