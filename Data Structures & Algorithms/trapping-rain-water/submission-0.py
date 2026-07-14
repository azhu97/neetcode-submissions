
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        # Compute prefix max array
        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])

        # Compute suffix max array
        suffix[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        # Calculate trapped water
        water = 0
        for i in range(n):
            water += min(prefix[i], suffix[i]) - height[i]

        return water
