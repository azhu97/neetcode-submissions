class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # o(n) space would use a counter to keep track
        # o(1) space would have to utilize the original nums array
        # we cannot sort
        # we can however scan x amount of time, given x is arbitarlly constant 
        count = defaultdict(int)
        res = 0
        for num in nums:
            count[num] += 1
            if count[num] > count[res]:
                res = num

        return res