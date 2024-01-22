#[1,3,2,7,6,9,0]
#calling the function recursively as the outer loop can be broken into smaller subproblems.


def bubble_sort(arr,end):
    #if end and start are 0, no more swaps possible,array of length 0 is already sorted.
    if(end==0):
        return
    for i in range(end):
        if(arr[i]>arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]
    
    #decrease the array by length 1 and then do the check and swap
    bubble_sort(arr,end-1)


l=[1,3,2,7,6,9,0,2]
bubble_sort(l,len(l)-1)
print(l)