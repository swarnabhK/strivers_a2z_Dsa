#Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

def linearSearch(nums,target):
    for i in range(len(nums)):
        if(nums[i]==target):
            return i
    return -1

arr = [1,2,3,4,5]
print(linearSearch(arr,3))
print(linearSearch(arr,6))
