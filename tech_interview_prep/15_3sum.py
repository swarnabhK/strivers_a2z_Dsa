# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# O(N**2)
# use 3 pointers. i,lo,hi. 
#[-4,-1,-1,0,1,2], i=4, lo = -1, hi = 2, check if nums[i]+nums[lo]+nums[hi]==0
class Solution:
    def threeSum(self, nums):
        res  = []
        # first sort the array.
        nums.sort()
        for i in range(len(nums)):
            # case when current element >0, we will never find three numbers that add to zero in this case so break.
            if nums[i]>0:
                break
            # if first element or element is not equal to previous element
            if i==0 or nums[i]!=nums[i-1]:
                lo,hi = i+1,len(nums)-1
                while(lo<hi):
                    #find sum
                    val = nums[lo]+nums[hi]+nums[i]
                    #if sum <0, means we need a higher number at lo, incrememt lo
                    if val<0:
                        lo = lo+1
                    elif val>0:
                    #if sum >0, means we need a smaller number at hi, decrement hi
                        hi = hi-1
                    else:
                      #sum is 0, then add the triplet to the res array.
                        res.append([nums[i],nums[lo],nums[hi]])
                        #look for the next set of triplets.
                        lo+=1
                        hi-=1
                        # we need to keep incrementing lo till it's not equal to it's previous element or we will get duplicate triplets in the result set.
                        while(lo<hi and nums[lo]==nums[lo-1]):
                            lo+=1
        return res
