# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



# [[1,3],[2,6],[8,10],[15,18]]
# we need to make sure that the list is sorted as per the first element.
# - start with 1,3
# merged = [[1,3]]
# - compare the first element of current interval, interval[0] with the last element(1) of the merged list, in this case 
# [[1,3]]'s [3] will be compared with [2,6]'s [2], since interval[0]<merged[-1][1], we will merge, so basically the last element in merged will be changed,can be , [1,7],[2,6] so in this case we will just find the max of (interval[1],merged[-1][1])

# -> not merge case is :
# 	if not merged or interval[0]>merged[-1][1] - > add current element to merged
# 	else: merge case
# 	change the last element in merged with the max of current interval last element and last merged element's last element.
# 	merged[-1][1] = max(interval[1],merged[-1][1])

class Solution:
    def merge(self, intervals):
        merged = []
        intervals.sort(key=lambda x:x[0])
        for interval in intervals:
            if not merged or interval[0]>merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1],merged[-1][1])
        return merged
  

