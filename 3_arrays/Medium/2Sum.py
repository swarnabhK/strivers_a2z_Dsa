# Problem Statement: Given an array of integers arr[] and an integer target.
# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.
# Example: N = 5, arr[] = {2,6,5,8,11}, target = 14, yes 6+8 = 14, so there exists two numbers with sum equals to target.

#approach 1: check each number with each other(using two for loops)
#TC: O(N**2)

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                return [i,j]
    return [-1,-1]

print(two_sum([2,6,5,8,11],14))


# approach 2: using a hashmap. We check the difference i+j = 14, 14-j = i, if we can prove target-number is present in the hashmap.
# means there are two numbers who add up to target.
# TC: O(N), SC: O(1)

def two_sum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        if (target-nums[i]) in hashmap:
            return [hashmap[target-nums[i]],i]  #hashmap contains {2:0,6:1,5:2...}{element:index}
        hashmap[nums[i]] = i
    return [-1,-1]

print(two_sum([2,6,5,8,11],14))