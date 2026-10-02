class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for sell in prices:
            if sell < minPrice:
                minPrice = sell
            else:
                maxProfit = max(maxProfit, sell - minPrice)
        
        return maxProfit