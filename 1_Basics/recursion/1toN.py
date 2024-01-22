#Print 1 to N using Recursion

def print_number(N):
    if(N==0):
        return
    print_number(N-1)
    print(N)

N = int(input("Enter N value to print 1 to N numbers: "))
print_number(10)