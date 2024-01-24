# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.
# Input: [100, 200, 1, 3, 2, 4]
# Output: 4
# Explanation: The longest consecutive subsequence is 1, 2, 3, and 4.
# TC: Putting elements on the set is O(N),then we need to check num-1 exists for every element O(N) and checking if the consecutive elements
# are present is O(N) roughly. So TC = O(N)


def longestConsecutive(nums):
    if(not nums):
        return 0
    #putting all the numbers in a set
    num_set = set(nums)
    maximum_length = 1
    for num in num_set:
        #checking if the number can be the start of a sequence.
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            #checking if num+1 exists in set, so that we can calculate the length of the sequence.
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            #checking if the current sequence is the longest sequence.
            maximum_length = max(maximum_length, current_length)
    return maximum_length



nums = [102,4,100,1,101,3,2,1,1]
print(longestConsecutive(nums))