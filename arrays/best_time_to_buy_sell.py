class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_1 = [0]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    min_1.append(prices[j]-prices[i])
        return max(min_1)

        