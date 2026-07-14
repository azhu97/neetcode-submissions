class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target >= nums[l] and nums[m] >= target:
                    print(1)
                    r = m - 1
                else:
                    print(2)
                    print(l, r)
                    l = m + 1
            else:
                if target >= nums[m] and target <= nums[r]:
                    print(3)
                    l = m + 1
                else:
                    print(4)
                    r = m - 1
        
        print(l, r)
        return -1