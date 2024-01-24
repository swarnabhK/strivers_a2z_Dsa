#approach1 : we will take an extra array and start storing all the elements from index 1 to end of array, and then store the first index in last index of new array, naive approach because we are using extra space.
#TC: O(N)
def leftRotateArray(arr):
    res = [0]*len(arr)
    j = 0
    for i in range(1,len(arr)):
        res[j] = arr[i]
        j+=1
    res[j] = arr[0]
    return res

arr = [1,2,3,4,5]
print(leftRotateArray(arr))

#Better approach without using extra space.
#TC: O(N)

def leftRotateArray2(arr2):
    temp = arr2[0]
    for i in range(len(arr2)-1):
        arr2[i] = arr2[i+1]
    arr2[-1] = temp

arr2 = [1,2,3,4,5]
leftRotateArray2(arr2)
print(arr2)

#approach 3: pythonic

def leftRotateArray_pythonic(arr):
    return arr[1:]+[arr[0]]

arr3 = [1,2,3,4,5]
print(leftRotateArray_pythonic(arr3))