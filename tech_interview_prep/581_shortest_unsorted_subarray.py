# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

# Return the shortest such subarray and output its length.


# O(nlogn), do this using stack for O(N), future work.
class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        st = sorted(nums)
        #pointers representing the start and end pointers for the original array(nums) and the sorted array st.
        l1,l2,r1,r2 = 0,0,len(nums)-1,len(st)-1
        while(l1<r1):
            # the moment we encounter the index where elements don't match for the two arrays.
            if(nums[l1]!=st[l2]):
                # we start iterating from the back till we find the index where both elements don't match.
                while(nums[r1]==st[r2]):
                    r1-=1
                    r2-=1
                #at this point we have the left boundary of the unsorted subarray and right boundary too. return the length.
                return r1-l1+1
            # if the elements at the start indexes are equal, we will just keep incrementing.
            l1+=1
            l2+=1
        return 0



