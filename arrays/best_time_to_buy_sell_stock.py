class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_1 = prices[0]
        profit =0
        for i in range(1,len(prices)):
            cost = prices[i]-min_1
            profit = max(profit,cost)
            min_1 = min(min_1,prices[i])
        return profit

        