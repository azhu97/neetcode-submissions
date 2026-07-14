class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_set = set(nums1)
        res = set()
        for num in nums2:
            if num in n1_set:
                res.add(num)
        
        return list(res)