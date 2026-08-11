class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        count = 0
        piles= sorted(piles)
        for i in range(len(piles)):
            a = piles[i]
            # print(a)
            for j in range(len(piles)):
                
                if(float(piles[j]/a)>int(piles[j]/a)):
                    count += int(piles[j]/a) +1
                count += int(piles[j]/a)
                
            if count<=h:
                return a
            elif count>h:
                count = 0 
        
        