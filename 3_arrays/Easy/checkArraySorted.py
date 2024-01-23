# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

def check_sorted(arr):
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            return False
    return True

l = [1,2,3,4,5,6,9,7,8]
l2 = [1,2,3,4,5,6,7,8,9]
print(check_sorted(l))
print(check_sorted(l2))