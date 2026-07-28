class Solution:
    def countSubstrings(self, s: str) -> int:
        def center(i):
            nonlocal s
            # returns the number of substring with center i
            res = 1 
            l, r = i - 1, i + 1
            if l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                if s[l] == s[r - 1]:
                    res += 1
                if s[l + 1] == s[r]:
                    res += 1
            print(i, res)
            return res
        
        res = 0
        for i in range(len(s)):
            res += center(i)
        
        
        return res
            