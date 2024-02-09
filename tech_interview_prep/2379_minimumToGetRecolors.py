# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

#Approach
# Find the no of W's in the window of size k. After that, at each iteration, add a W if the next block is a W and remove a W from the left if the left pointer points to a W. Check if the W count at the current iteration is lesser than the current minimum.


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        no_w,left = 0,0
        for i in range(k):
            no_w+=1 if blocks[i]=='W' else 0
        res = no_w
        for right in range(k,len(blocks)):
            no_w+=1 if blocks[right]=='W' else 0
            no_w-=1 if blocks[left]=='W' else 0
            left+=1
            res = min(no_w,res)
        return res


