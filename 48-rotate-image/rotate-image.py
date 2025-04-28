class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(len(matrix)//2):
            for j in range(i,length-i-1,1):
                temp=matrix[i][j]
                matrix[i][j] = matrix[length-j-1][i]
                matrix[length-j-1][i] = matrix[length-i-1][length-j-1]
                matrix[length-i-1][length-j-1] = matrix[j][length-i-1]
                matrix[j][length-i-1] = temp
        
