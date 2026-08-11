class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        eating_speeds = sorted(piles)
        
        # 1 2 3 4 

        left, right = 0, len(piles) -1 

        k_rates_lst = []

        while(left <= right):
            mid_point = (left+right)//2 

            k_rate = eating_speeds[mid_point]

            time_to_eat = 0 

            for i in piles: 
                if i % k_rate == 0:
                    time_to_eat += int(i/k_rate)
                elif i % k_rate != 0:
                    time_to_eat += int((i/k_rate) + 1)
            print(time_to_eat)
            if time_to_eat > h: #eating too slow
                left = mid_point + 1 

            elif time_to_eat < h: #eating way too fast
                k_rates_lst.append(k_rate)
                right = mid_point - 1 
            
            elif time_to_eat == h: 
                return k_rate

        return sorted(k_rates_lst)[0]


        



        

        