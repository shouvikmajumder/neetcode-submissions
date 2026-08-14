class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Problem Approach:
                
                Naturally I believe a sliding window is the best approach to this problem

                we know that in order to have a profit the price on the right pointer 
                is going to have to be bigger that the price at the left pointer 

                we can keep track of the maxproft we have seen so far as well

                however, if this is not the case, we have to push the left pointer 
                to where the right pointer is, since it is the the next smallest value
        '''

        max_prof = 0
        left = 0    

        for right in range(len(prices)): 
            
            if prices[right] > prices[left]: 
                prof = prices[right] - prices[left]
                max_prof = max(max_prof,prof)
            else: 
                left = right
    
        return max_prof
