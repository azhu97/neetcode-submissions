class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        arr = None
        while low <= high:
            if target < matrix[low][0] or target > matrix[high][-1]:
                return False
            mid = (low + high) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                print(1)
                arr = matrix[mid]
                break
            if matrix[mid][-1] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return True
            if arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
            
