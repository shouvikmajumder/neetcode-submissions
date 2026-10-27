class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0 
        left = 0    

        for right in range(len(prices)):

            while prices[left] > prices[right]:
                left += 1 
            
            if prices[right] > prices[left]:
                res += (prices[right] - prices[left])
                left = right
        
        return res