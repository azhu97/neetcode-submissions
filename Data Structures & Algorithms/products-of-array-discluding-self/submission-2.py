class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = array of integers
        # return output arr, where output[i] = product of all nums
        # very easy to do in O(n^2) time, but we must do it in O(n) time
        # we can keep a running product, going both ways
        up = [1 for i in range(len(nums))]
        down = up.copy()
        for i in range(len(nums)):
            # update up
            up[i] = nums[i] * (up[i - 1] if i > 0 else 1)
            down[-1 - i] = nums[-1 - i] * (down[-i] if i > 0 else 1)
        print(up)
        print(down)
            
        res = []
        for i in range(len(nums)):
            l, r = up[i - 1] if i > 0 else 1, down[i + 1] if i < len(nums) - 1 else 1
            print(i)
            print(l, r)
            res.append(l * r)
        
        return res
            
        