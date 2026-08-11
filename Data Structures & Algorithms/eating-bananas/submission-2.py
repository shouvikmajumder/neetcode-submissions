class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            time = 0
            for i in piles: 
                if int(i/speed) < float(i/speed):
                    time += int(i/speed) + 1
                else:
                    time += int(i/speed)
            if time <= h:
                return speed
            else:
                speed +=1 

                