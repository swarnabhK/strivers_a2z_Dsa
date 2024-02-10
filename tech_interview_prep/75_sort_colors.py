# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


from collections import Counter
class Solution:
    def sortColors(self, nums):
        # Dutch national flag algorithm to sort in place O(N)
        # can be used to sort three numbers. (0,1,2)
        # lo, to keep track of the position where next zero needs to be set,
        # i to iterate over the array
        # hi, to keep track of the position where next 2 needs to be set.
        # if i==0, swap element at lo and i, iterate lo, and i.
        # if i==1, do nothing just iterate i
        # if i==2, swap element at high and i, after swap element at i can be 0 or 1
        # so just decrement hi
        lo,i,hi = 0,0,len(nums)-1

        # why? is i<=hi? the moment we reach i==hi, means we are in the 2 territory, we don't need to make any more swaps.
        while(i<=hi):
            #case nums[i]==0
            if nums[i]==0:
                #swap lo and i
                nums[lo],nums[i] = nums[i],nums[lo]
                i+=1
                lo+=1
            elif nums[i]==1:
                #do nothing
                i+=1
            else:
                #if nums==2, after swapping we don't increment i because after swap the current element may be a 0/1 , we need to check i again.
                #swap i and hi
                nums[i],nums[hi] = nums[hi],nums[i]
                hi-=1