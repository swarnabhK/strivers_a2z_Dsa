#Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k

# Sliding window can be used. Hint: Subarray, find longest, sum=k
#left pointer and right pointer. Rp will iterate through the array, once the condition becomes invalid we will shrink the window(reduce left pointer)
# until the window becomes valid again, once the window is valid we will do the remaining operations. In this case : check if the windo is the longest

#example : {2,3,5,1,9}, k = 10

def longest_subarray(nums,k):
    left,curr,max_window = 0,0,0
    for right in range(len(nums)):
        curr+=nums[right]
        while(curr>k):
            curr-=nums[left]
            left+=1
        if(curr==k):
            if(right-left+1>max_window):
                max_window = right-left+1
                mx = nums[left:right+1]
    return mx,max_window


print(longest_subarray([2,3,5,1,9],10))
print(longest_subarray([1,2,3,1,1,1,1,4,2,3],3))