# Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

# For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].


def subarray_sum(nums,queries,limit):
  #result to store the query answers
  res = []
  #first find the prefix sum
  prefix = [nums[0]]
  for i in range(1,len(nums)):
    prefix.append(nums[i]+prefix[-1])
  # for each query find if the sum of the subarray represented by the query is smaller than limit.
  for x,y in queries:
    #10,14,12
    sub_sum = prefix[y]-prefix[x]+nums[x]
    res.append(sub_sum<limit)
  return res

print(subarray_sum([1, 6, 3, 2, 7, 2],[[0, 3], [2, 5], [2, 4]],13))