# Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
#arr[] = {4,1,2,1,2}
#approach 1: xor of two equal numbers will be 0, so : (1^1)^(2^2)^(4) = (0)^4 = 4(so the one element which appears once will be left)
#TC : O(N), no extra space required so SC: O(1)

from collections import defaultdict
def appearsOnce(arr):
    xor = 0 #we can start with xor equals 0 because after the first xor iteration, the xor will be equal to the array element at index 0
    for i in range(len(arr)):
        xor = xor^arr[i]
    return xor


print(appearsOnce([4,1,2,1,2]))

#approach 2: using hashmap
#TC: O(N)+O(N), SC: O(N)
def appearsOnce_2(arr):
    dict = defaultdict(int)
    for num in arr:
        dict[num]+=1
    for num in dict:
        if dict[num]==1:
            return num

print(appearsOnce_2([4,1,2,1,2]))


#using hasharray, cannot use this approach in case of negative numbers and should not use for large values(because the hasharray will be large in that case)
#TC: O(N)+O(N), SC: O(1)
def appearsOnce_3(arr):
    length = max(arr)+1 #length of the hasharray
    hasharray = [0]*length
    for i in range(len(arr)):
        hasharray[arr[i]]+=1 #increment the value of element at index i in the hasharray
    for i in range(len(hasharray)):
        if(hasharray[i]==1):
            return i
  
print(appearsOnce_3([4,1,2,1,2]))