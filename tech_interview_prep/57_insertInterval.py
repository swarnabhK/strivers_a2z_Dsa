class Solution:
    def insert_position(self,intervals,newInterval):
        # this returns the index of the element just bigger than newInterval in the
        # intervals list, this is the insert position we need.
        start,end = 0,len(intervals)-1
        while(start<=end):
            mid = (start+end)//2
            if(intervals[mid][0]>newInterval[0]):
                end = mid-1
            else:
                start = mid+1
        return start
    def insert(self, intervals, newInterval):
        if not intervals:
          return [newInterval]
        #use binary search to find insert position of the new interval.
        ip = self.insert_position(intervals,newInterval)
        intervals.insert(ip,newInterval)
        #now in this new intervals, merge the intervals.
        merged = []
        for interval in intervals:
            #not merge case
            if not merged or interval[0]>merged[-1][1]:
                merged.append(interval)
            else:
                #merge case
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged


obj = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(obj.insert(intervals,newInterval))