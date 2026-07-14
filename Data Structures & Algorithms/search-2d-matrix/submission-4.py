class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search for row first
        low, high = 0, len(matrix) - 1
        arr = []
        while low <= high:
            mid = (high + low) // 2
            if target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                break
        
        if (low > high):
            return False
        row = mid

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False



        