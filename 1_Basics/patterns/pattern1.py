""" Print a pattern like  * * *
                          * * *
                          * * * , for n=3    """


def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end = " ")
        print()

print("Printing pattern: ")
pattern(3)
print("Printing pattern: ")
pattern(5)
