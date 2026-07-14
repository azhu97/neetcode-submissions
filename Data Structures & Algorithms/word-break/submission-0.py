class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp problem
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(dp)):
            for word in wordDict:
                start = i - len(word)
                if start >= 0 and dp[start] and s[start:i] == word:
                    dp[i] = True
                    break
        
        return dp[-1]

        