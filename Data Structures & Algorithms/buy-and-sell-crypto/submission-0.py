class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Input: prices = [10,1,5,6,7,1]
        # buy 1, sell 7, prof = 6
        # 10, 1

        memo = {}
        def prof(prices, i, j):
            if i >= j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = max(prof(prices, i, j - 1), prof(prices, i + 1, j), prices[j] - prices[i])
            return memo[(i, j)]

        max_profit = prof(prices, 0, len(prices) - 1)
        return max_profit