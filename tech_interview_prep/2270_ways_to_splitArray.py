# You are given a 0-indexed integer array nums of length n.
# nums contains a valid split at index i if the following are true:
#     The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
#     There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

def waysToSplitArray(nums):
    prefix = [nums[0]]
    splits = 0
    #find prefix sum
    for i in range(1,len(nums)):
        prefix.append(nums[i]+prefix[-1])
    #start from 0, find left half sum and find right half sum
    for i in range(len(nums)-1):
        right_half = prefix[-1]-prefix[i]
        left_half = prefix[i]
        if(left_half>=right_half):
            splits+=1
    return splits


print(waysToSplitArray([1, 2, 2, 2, 5, 0]))  # Output: 2
