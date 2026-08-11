class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        eating_speeds = sorted(piles)[-1]
        
        # 1 2 3 4 

        left, right = 1, eating_speeds

        while(left <= right):
            mid_point = (left+right)//2 

            k_rate = mid_point

            time_to_eat = 0 

            for i in piles: 
                if i % k_rate == 0:
                    time_to_eat += int(i/k_rate)
                elif i % k_rate != 0:
                    time_to_eat += int((i/k_rate) + 1)

            if time_to_eat > h: #eating too slow
                left = mid_point + 1 
            else: 
                right = mid_point - 1 

        return left 
        


        



        

        