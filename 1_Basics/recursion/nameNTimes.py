#Print Name N times using Recursion

def print_name(name,N):
    if(N==0):
        return
    print(name)
    print_name(name,N-1)


print_name("Swarnabh",4)