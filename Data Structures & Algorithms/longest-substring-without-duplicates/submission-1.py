class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        l = 0
        r = 0 
        
        temp = set()
        answer = 0 
        while r < len(s):
            if s[r] in temp:
                answer = max(answer, r - l)
                while s[l] != s[r]:
                    temp.remove(s[l])
                    l += 1
                temp.remove(s[l])
                l += 1
            else:
                temp.add(s[r])
                r += 1
                if r == len(s):
                    answer = max(answer, r - l)
        return answer
            
