class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2 # bannas per hour
            print(m)
            total_hours = 0
            for pile in piles:
                if pile % m == 0:
                    total_hours += pile // m
                else:
                    total_hours += pile // m + 1
            print("total hours", total_hours)
            if total_hours <= h:
                res = min(res, m) # this also means that we can pot go lower
                r = m - 1
            else:
                l = m + 1
        
        return res
