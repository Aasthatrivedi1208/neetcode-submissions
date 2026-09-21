class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy=prices[0]
        maxprofit=0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]>minBuy:
                profit=prices[i]-minBuy
            maxprofit=max(maxprofit,profit)
            minBuy=min(minBuy,prices[i])
        return maxprofit

        