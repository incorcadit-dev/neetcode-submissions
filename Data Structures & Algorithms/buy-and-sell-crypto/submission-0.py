class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maximum = max(maximum, profit)
            else:
                l = r
        return maximum
        
            
        