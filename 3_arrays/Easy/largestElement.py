#find the maximum element in an array

#brute force: sort the array and return the last element in the array.
#TC: O(NlogN)
def largest(arr):
    arr.sort()
    return arr[-1]


l = [1,34,5,6,9,13,8,24]
print(largest(l))

#Using a max variable to keep track of the maximum value seen till now.
#TC: O(N)
def largest2(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>max):
            max = arr[i]
    
    return max
print(largest2(l))

#using recursion
def largest_rec(arr):
    def helper(arr,m,start,n):
      if(start>=n):
          return m
      if(arr[start]>m):
          m = arr[start]
      return helper(arr,m,start+1,n)
    return helper(arr,arr[0],1,len(arr))

arr = [1,34,5,6,9,13,8,24]
print(largest_rec(arr))
    