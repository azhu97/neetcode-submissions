class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        marking = [False for i in range(n)]

        def rec(arr, marking):
            if len(arr) == n: # if maxed out, add to res
                res.append(arr.copy())
                return 
            for i in range(n):
                if marking[i]: # this is already in use so go to next
                    continue
                marking[i] = True # otherwise we continue with the marking 
                arr.append(nums[i])
                rec(arr, marking)
                arr.pop()
                marking[i] = False
        
        rec([], marking)
        return res 