
#approach1 (Using sort),only if there are no duplicate elements in the array.
def second_largest1(arr):
    arr.sort()
    return arr[-2]

l = [1,34,5,6,9,13,8,24]
print(second_largest1(l))


#approach2 : two pass solution to find the first and then the second largest
#TC: O(N)
def second_largest2(arr):
    largest = float("-inf")
    smallest = float("inf")
    second_smallest = float("inf")
    second_largest = float("-inf")
    for i in range(len(arr)):
        if(arr[i]>largest):
            largest = arr[i]
        if(arr[i]<smallest):
            smallest = arr[i]
    for i in range(len(arr)):
        if(arr[i]>second_largest and arr[i]!=largest):
            second_largest = arr[i]
        if(arr[i]<second_smallest and arr[i]!=smallest):
            second_smallest = arr[i]
    return second_smallest,second_largest

l = [1,34,5,6,9,13,8,24] 
second_smallest,second_largest = second_largest2(l)
print(second_smallest,second_largest)


#approach 3, in one pass-> if we find a number lesser than small, then new small will be that number and second smallest will be small
#O(N) but just one pass
def second_smallest(arr):
    small,second_small = float("inf"),float("inf")
    for i in range(len(arr)):
        if(arr[i]<small):
            second_small = small
            small = arr[i]
        elif(arr[i]<second_small):
            second_small = arr[i]
    return second_small
l2 = [0,1,34,5,6,9,13,8,24]
print(second_smallest(l2))
