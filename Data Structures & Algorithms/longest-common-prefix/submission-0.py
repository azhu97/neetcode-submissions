class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # longest common prefix
        short = float('inf')
        word = None
        for w in strs:
            if len(w) < short:
                short = len(w)
                word = w
        
        def function(short, long):
            res = 0 
            for i in range(len(short)):
                if short[i] != long[i]:
                    return res
                res += 1
            return res

        res = float('inf')
        for w in strs:
            res = min(res, function(word, w))
        
        return word[:res]