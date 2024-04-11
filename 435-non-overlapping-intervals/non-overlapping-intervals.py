class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        length = len(intervals)
        intv_s = intervals[0][0]
        intv_e = intervals[0][1]
        cnt = 0
        for i in range(1,length):
            if intervals[i][0]<intv_e:
                cnt +=1
            else:
                intv_s = intervals[i][0]
                intv_e = intervals[i][1]
        return cnt