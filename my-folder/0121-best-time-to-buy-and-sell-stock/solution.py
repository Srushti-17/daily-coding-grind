class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, max_pro = prices[0], 0
        for price in prices:
            mini = min(mini,price)
            profit = price - mini
            max_pro = max(max_pro,profit)

        return max_pro
