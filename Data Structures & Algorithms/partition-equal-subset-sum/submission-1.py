class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total / 2
        print(f"Half: {half}")

        res = False
        def bfs(i, tot):
            # print(tot)
            nonlocal half 
            nonlocal res
            # two options, include i, or don't include i
            # we must explore both
            if tot == half:
                res = True
                return 
            if i >= len(nums) or tot > half:
                return 
            # include i
            tot += nums[i]
            bfs(i + 1, tot)
            tot -= nums[i]
            # don't include i
            bfs(i + 1, tot)
        
        bfs(0, 0)
        return res