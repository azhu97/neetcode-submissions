class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = max(right, arr[i])
            arr[i] = right
            right = temp
        return arr
        