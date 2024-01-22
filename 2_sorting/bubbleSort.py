#[13,46,24,52,20,9]
# 1) in one iteration, check neighbor elements. If arr[i]>arr[i+1], we swap. the outer loop iteration will be till len(arr)-1
# after every iteration the last element will be sorted. 

#Time complexity: O(N**2)
def bubble_sort(arr):
    for i in range(len(arr),1,-1):
        for j in range(i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]


# l = [13,46,24,52,20,9]
# bubble_sort(l)
# print(l)


#approach 2 using while loop, better approach, We are breaking out after first iteration if we see no swaps happening, that is the array is already sorted.
#Best case O(N)
def bubble_sort2(arr):
    end = len(arr)-1
    didSwap = False
    for _ in range(len(arr)):
        j = 0
        while(j<end and end>0):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                didSwap = True
            j+=1
        if(not didSwap):
                print("The array is already sorted")
                break
        end-=1

l2 = [13,46,24,52,20,9]
bubble_sort2(l2)
print(l2)

#already sorted case
l3 = [1,2,3,4,5]
bubble_sort2(l3)
print(l3)

l4 = [13,46,24,52,20,9,9,13,46]
bubble_sort2(l4)
print(l4)