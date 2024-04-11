class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0],-x[1]))
        comm_e=points[0][1]
        cnt = 1
        for pt in points:
            # if pt[0]>comm_s and pt[0]<=comm_e:
                # comm_s=pt[0]
            if pt[1]<=comm_e:
                comm_e=pt[1]
            if pt[0]>comm_e:
                comm_e=pt[1]
                cnt+=1
        return cnt