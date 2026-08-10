class Solution:

    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        # dp[i] represents decoding ways for prefix of length i
        dp = [0] * (n + 1)
 
        # Base cases
        dp[0] = 1  # Base case for empty prefix matching two-digit decodes
        dp[1] = 1  # First char is non-zero (checked above)

        for i in range(2, n + 1):
            # Check single digit (s[i-1])
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # Check two digits (s[i-2:i])
            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]