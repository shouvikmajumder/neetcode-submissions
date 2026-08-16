class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Problem Approach: 
                We are going to use a sliding window
                
                In order to make profit the value of our right pointer must be bigger than 
                our left pointer value

        '''
        max_prof = 0

        left = 0

        for right in range(len(prices)):
            if prices[right] >= prices[left]: 
                curr_prof = prices[right] - prices[left]
                max_prof = max(max_prof,curr_prof)
            elif prices[right] < prices[left]:
                left = right
        
        return max_prof