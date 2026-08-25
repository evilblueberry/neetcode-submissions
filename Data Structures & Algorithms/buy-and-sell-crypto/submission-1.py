class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]

        for sell in prices:
            if buy > sell:
                buy = sell
            else:
                res = max(res, sell-buy)
        return res