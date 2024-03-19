class Solution(object):
    def equalPairs(self, grid):
        cnt = 0
        length = len(grid)
        col = []
        for i in range(length):
            for j in range(length):
                col += [grid[j][i]]
            for row in grid:
                if col == row:
                    cnt+=1
            col = []
        return cnt
        