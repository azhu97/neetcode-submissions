class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []
        
        def recurse(i):
            if i >= len(nums):
                res.append(temp.copy())
                return
            
            temp.append(nums[i])
            recurse(i + 1)
            temp.pop()
            recurse(i + 1)
        
        recurse(0)
        return res
            
        
        

        