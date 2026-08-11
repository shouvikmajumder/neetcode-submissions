import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)

        ValidMinEatingSpeed = []
        
        while left <= right: 
            eating_speed = (left + right ) // 2

            current_hours = 0

            for bananas in piles: 
                current_hours += math.ceil(bananas / eating_speed)

            if current_hours > h: 
                # eating too slow
                left = eating_speed + 1
            elif current_hours == h: 
                # slowest you could possibly go
                return eating_speed  
            elif current_hours < h :
                #eating too fast 
                ValidMinEatingSpeed.append(eating_speed)
                right = eating_speed - 1     
        
        print(ValidMinEatingSpeed) 
        return min(ValidMinEatingSpeed)
