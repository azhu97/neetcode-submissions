class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i, num in enumerate(nums):
            left = nums[i - 1] if i - 1 >= 0 else 1
            right = nums[i + 1] if i + 1 <= n - 1 else 1
            dp[i][i] = num * left * right
        # for d in dp: print(d)
        for j in range(n):
            for i in range(j, -1, -1):
                if i >= j:
                    continue
                # print(f"At coord: {i}, {j}")
                for p in range(i, j):
                    # if we are finding the pivot point p, one of the halves has to go first
                    # so it won't be completely accurate
                    # we have to factor out the neighbor being removed first
                    # print(f"p = {p}")
                    first_half_first = dp[i][p] + (dp[p + 1][j] / nums[p] * (nums[i - 1] if i - 1 >= 0 else 1))
                    # print(f"first half first value = {first_half_first}")
                    second_half_first = (dp[i][p] / nums[p + 1] * (nums[j + 1] if j + 1 <= n - 1 else 1)) + dp[p + 1][j]
                    # print(f"second half first value = {second_half_first}")
                    dp[i][j] = max(dp[i][j], first_half_first, second_half_first)
        # for d in dp: print(d)
        return int(dp[0][-1])