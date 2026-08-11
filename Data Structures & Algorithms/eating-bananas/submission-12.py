import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # optimize for k (smallest)

        max_k_val = max(piles)

        valid_k = []

        left, right = 1, max_k_val
        while left <= right: 

            k_val = (left + right )// 2
            
            counter = 0

            for i in piles: 
                
                counter += math.ceil(i/k_val)
            
            if counter <= h: # eating too fast
                valid_k.append(k_val)
                right = k_val - 1
            
            elif counter > h: #eating too slow
                left = k_val + 1 
                

        return min(valid_k)
        

