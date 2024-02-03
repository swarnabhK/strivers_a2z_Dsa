# If you start from the top left corner of a m*n grid, find the number of ways to travel to the bottom right corner.
# to reach the bottom right corner, you can only tavel either right or down.
# first intuition that comes to my mind is there are two options: go down or go right, taking any option reduces the problem into two subproblems.
# That means we can use recursion.


def gridTravel(row,col,cache={}):
    # we are passing the cache dictionary between different recursive calls, memoization.
    if (row,col) in cache:
        return cache[(row,col)]
    if row==0 or col==0:
        return 0
    if row==1 and col==1:
        return 1
    #travel down case + #travel right case
    res = gridTravel(row-1,col,cache)+gridTravel(row,col-1,cache)
    cache[(row,col)] = res
    return res

print(gridTravel(2,3)) #3
print(gridTravel(1,1)) #1
print(gridTravel(3,2)) #3
print(gridTravel(3,3)) #6
print(gridTravel(18,18)) #this case long time if we use simple recursion, we need to memoize to not repeat the overlapping subproblems. 2333606220