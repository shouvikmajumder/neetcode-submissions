class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof = 0 

        left = 0

        for right in range(len(prices)):
            if prices[right] > prices[left]:
                max_prof += (prices[right] - prices[left])

            while left < right:
                left += 1

        return max_prof
