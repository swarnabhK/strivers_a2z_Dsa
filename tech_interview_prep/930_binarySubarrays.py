from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums, goal) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr,total = 0,0
        for num in nums:
            curr+=num
            # checking how many subarrays with a prefix sum of diff has occured till the current index, if sum till index i is s, and we assume that there are subarrays with sum k ending at this position, then checking no of occurences of s-k, gives us number of subarrays with sum k. 
            if(curr-goal in prefix):
                total+=prefix[curr-goal]
            prefix[curr]+=1
        return total