# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

#Approach 1
#TC: O(N), SC: O(1)
#slow pointer to  fill all non zero elements first. once the non zero elements are filled, fill the rest of the array with 0.
def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if(nums[fast]!=0):
            nums[slow] = nums[fast]
            slow+=1
    while(slow<len(nums)):
        nums[slow]=0
        slow+=1

l = [1,0,2,3,0,4,0,1]
moveZeroes(l)
print(l)


#Approach 2: Brute force solution
#TC: O(N), SC: O(N)
def moveZeroes2(nums):
    temp = []
    #fill temp array with non zero elements first
    for i in range(len(nums)):
        if(nums[i]!=0):
          temp.append(nums[i])
    #fill the non zero elements in the firts half of nums
    for i in range(len(temp)):
        nums[i] = temp[i]
    i+=1
    #fill the remaining half of nums with 0
    while(i<len(nums)):
        nums[i]=0
        i+=1
  

l2 = [1,0,2,3,0,4,0,1]
moveZeroes2(l2)
print(l2)