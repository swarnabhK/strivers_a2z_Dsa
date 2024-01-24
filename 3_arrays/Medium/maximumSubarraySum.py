

#Approach 1: finding all the subarrays and finding their sum, keeping track of the maximum sum. 
def maximumSubarraySum(nums):
    maxi = float("-inf")
    for i in range(len(nums)):
        s = 0
        for j in range(i,len(nums)):
            s+=nums[j]
            maxi = max(s,maxi)
    return maxi
nums = [-2,-3,4,-1,-2,1,5,-3]
print(maximumSubarraySum(nums))

#approach2: Kadane's algorithm, which states that if at any point the sum becomes negative, make sum zero. 
# why? Becuase if you carry over a negative sum, the sum will never expand.

def maximumSubarraySum2(nums):
    maxi = float("-inf")
    s = 0
    for i in range(len(nums)):
        s+=nums[i]
        if(s>maxi):
            maxi = s
        if(s<0):
            s = 0
    return maxi if maxi>0 else 0

print(maximumSubarraySum2([-2,-3,4,-1,-2,1,5,-3]))
print(maximumSubarraySum2([-2,-3,-4,-1]))
