# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

# If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

# Note: Return k after placing the final result in the first k slots of the array.


def removeDups(arr):
  i = 0
  for j in range(1,len(arr)):
      if(arr[i]!=arr[j]):
          i+=1
          arr[i] = arr[j]
  return i+1
arr = [1,1,2,2,2,3,3]
print(removeDups(arr))