class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(x):
            res = 0
            for i in range(32):
                if (1 << i) & x:
                    res += 1
            return res

        res = []
        for i in range(n + 1):
            res.append(count(i))
        
        return res
        