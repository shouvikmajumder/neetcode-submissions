class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        if prices == sorted(prices)[::-1]:
            return 0
        else: 
            l,r = 0,1
            maxprof = 0
            while(r<len(prices)):
                if prices[r] - prices[l] < 0: 
                    l = r
                    r += 1
                elif prices[r] - prices[l] > 0: #making profit
                    maxprof = max(maxprof,prices[r] - prices[l])
                    r += 1
                else: 
                    r += 1
            return maxprof