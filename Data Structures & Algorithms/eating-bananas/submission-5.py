class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, sorted(piles)[-1]
        
        while(left<=right):
            mp = (left+right )//2
            time = 0
            
            for i in piles:
                time += math.ceil(i/mp) #time to eat the pile
            # print(time)
            if time == h: 
                return mp
            if time <= h: #what heppens when the mp is too fast
                right = mp - 1
            else:
                left = mp + 1


        
        return left