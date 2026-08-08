class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find the lngth of the longest substring without duplicates chars
        # we can keep a window 
        # keep a set 
        # expand r when we have duplicates 
        # expand l when we have duplicates 
        chars = set()
        l, r = 0, 0
        res = 0 
        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res

                
            