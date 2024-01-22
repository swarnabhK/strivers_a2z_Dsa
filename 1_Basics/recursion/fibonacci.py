#iterative method

#nth fibonnaci number, find 50th fibonacci number
#naive approach, here space complexity is O(N) as we are using an array to hold the nth fibonacci number, we got to initialize the array.

def fib(n):
    if(n<1):
      return n
    fibo = [0]*n # creating an array of size n
    fibo[0],fibo[1] = 0,1
    for i in range(2,n):
        fibo[i] = fibo[i-1]+fibo[i-2]
    return fibo[n-1]


print(fib(6)) #nth fibonacci number.


#better approach, SC: O(1) we are not using any extra space except a few variables which means its constant space complexity

def fib_2(n):
    if(n<1):
        return n
    secondLast,last = 0,1
    for i in range(2,n):
        curr = last+secondLast
        secondLast = last
        last = curr
    return curr
print(fib_2(6))


#recursion
#fib(n) -> fib(n-1)+fib(n-2) parameterized recusrion

def fib_recursion(n,first,second,s):
    if(n==1):
        return s
    s = first+second
    second = first
    first = s
    return fib_recursion(n-1,first,second,s)

print(fib_recursion(6,0,1,0))


#recursion
#fib(n) -> fib(n-1)+fib(n-2) functional recursion

def fib_recursion2(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fib(n-1)+fib(n-2)

print(fib_recursion2(7))