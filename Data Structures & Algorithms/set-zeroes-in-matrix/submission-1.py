class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for b in matrix:
            print(b)
        def set_zero(coord):
            u, v = coord
            # set the row first
            for j in range(len(matrix[0])):
                matrix[u][j] = None
            for i in range(len(matrix)):
                matrix[i][v] = None
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    set_zero((i, j))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
        
