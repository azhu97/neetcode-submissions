class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # we can replicate a 90 degree clockwise by 
        # 1. reflecting the upper left and bottom right of the square
        # 2. reflecting down the middle
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i + j >= n:
                    continue
                # time to swap
                print(i, j)
                matrix[i][j], matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1], matrix[i][j]
        
        # reflect over middle line
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        