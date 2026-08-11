class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof = 0

        left = 0 

        for right in range(len(prices)):
            if prices[right] - prices[left] < 0:
                left = right
            
            print(prices[right] - prices[left])
            
            max_prof = max(max_prof, prices[right] - prices[left])
        
        
        return max_prof