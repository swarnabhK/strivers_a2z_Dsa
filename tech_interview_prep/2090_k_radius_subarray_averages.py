class Solution:
    def getAverages(self, nums, k):
        prefix = [nums[0]]
        avg = [-1]*len(nums)
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        for i in range(k,len(nums)-k):
            start = i-k
            end = i+k
            sub_sum = prefix[end]-prefix[start]+nums[start]
            avg[i] = (sub_sum)//(end-start+1)
        return avg

# Test case
solution = Solution()
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 3
print(solution.getAverages(nums, k))
