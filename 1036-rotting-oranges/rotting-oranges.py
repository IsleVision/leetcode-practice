class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        i_len = len(grid)
        j_len = len(grid[0])
        for i in range(i_len):
            for j in range(j_len):
                if grid[i][j]==2:
                    rotten +=[[i,j,0]]
        di = [[1,0],[-1,0],[0,1],[0,-1]]
        time = 0
        while rotten:
            i,j,t = rotten.pop(0)
            time = t
            for d in di:
                i_new = i+d[0]
                j_new = j+d[1]
                if 0<=i_new<i_len and 0<=j_new<j_len and grid[i_new][j_new]==1:
                    rotten += [[i_new, j_new, t+1]]
                    grid[i_new][j_new]=2
        for i in range(i_len):
            for j in range(j_len):
                if grid[i][j]==1:
                    return -1
        return time


