# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


# O(N**2)
class Solution:
    def threeSumClosest(self, nums, target):
        min_diff = float("inf")
        closest_sum = 0
        nums.sort()
        
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                  #find the current sum.
                current_sum = nums[i] + nums[lo] + nums[hi]
                # calculate how close teh sum is to the target, diff gives us that
                diff = abs(target - current_sum)
                
                # if diff is lower than the current diff, means we got a closer sum to target, so we will update closest sum.
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = current_sum
                
                # if sum is < target, we need to go towards target so we will increment lo, need a bigger number at lo
                if current_sum < target:
                    lo += 1
                # if sum is > target, we need a smaller number at hi, to go towards target, decrement hi.
                elif current_sum > target:
                    hi -= 1
                else:
                # if sum =target, means diff is equal to 0, that's the closest we can get to target. return the current sum(target).
                    return closest_sum
        return closest_sum
