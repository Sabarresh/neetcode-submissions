class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        maxProfit = 0

        while l < len(prices):
            for r in range(l+1, len(prices)):
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            
            l += 1
        
        return maxProfit