class Solution:
    def minStartValue(self, nums):
        total, min_val = 0, 0
        for num in nums:
            total += num
            if total < min_val:
                min_val = total
        return 1 - min_val

# Instantiate the Solution object
solution = Solution()

# Test case
nums = [1, 2, 3]

# Test the minStartValue method with the test case
print(f"Minimum Starting Value: {solution.minStartValue(nums)}")
