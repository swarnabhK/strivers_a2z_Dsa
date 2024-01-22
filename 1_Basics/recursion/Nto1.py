# print N to 1

def print_number(N):
    if(N==0):
        return
    print(N)
    print_number(N-1)

print_number(10)