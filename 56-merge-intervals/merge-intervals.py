class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[[intervals[0][0],intervals[0][1]]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=res[-1][1]:
                res[-1]=[res[-1][0],max(res[-1][1],intervals[i][1])]
            else:
                res+=[[intervals[i][0],intervals[i][1]]]
        return res

        