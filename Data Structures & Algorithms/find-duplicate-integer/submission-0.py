class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = set()
        for num in nums:
            if num in temp:
                return num
            else:
                temp.add(num)
        
        