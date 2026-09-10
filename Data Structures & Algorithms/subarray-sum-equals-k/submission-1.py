class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # subarrays are nonempty contigious sequence of elements 
        # give nums<arr> and k<int> return number of subarrays equal to k
        # prefix of number of times a running sum has been previous constructed
        # prefix<running_sum>, times running sum has occured previous>
        # from this, we can add to res, prefix[current_sum - k] 

        prefix = defaultdict(int)
        running = 0 
        res = 0
        prefix[0] += 1
        
        for num in nums:
            running += num
            target = running - k
            res += prefix[target]
            prefix[running] += 1
        
        return res