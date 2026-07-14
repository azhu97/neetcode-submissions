class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        res = 0
        for price in prices:
            min_buy = min(min_buy, price)
            res = max(res, price - min_buy)

        return res