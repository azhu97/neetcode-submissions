class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l_max, r_max = 0, 0
        l, r = 0, len(height) - 1
        while l <= r:
            l_max, r_max = max(l_max, height[l]), max(r_max, height[r])
            min_wall = min(l_max, r_max)
            if height[l] < height[r]:
                water += min_wall - height[l] if min_wall - height[l] > 0 else 0
                l += 1
            else:
                water += min_wall - height[r] if min_wall - height[r] > 0 else 0 
                r -= 1
        return water
        