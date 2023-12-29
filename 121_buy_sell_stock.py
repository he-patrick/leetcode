#  O(n^2) solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        n = len(prices)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > bestProfit:
                    bestProfit = prices[j] - prices[i]

        return bestProfit
    
# O(n) solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(prices[r] - prices[l], maxProfit)
            else:
                l = r
            r += 1
        
        return maxProfit