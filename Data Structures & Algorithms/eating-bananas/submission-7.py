class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right= 1, sorted(piles)[-1]

        while(left<=right):
            mp = (left+right)//2
            time =0 
            for i in piles:
                time += math.ceil(i/mp)
            #need to find the min eat speed
            if time<=h:
                #can slow it down to get a smaller k 
                right= mp -1
            else:
                #time is going to be too slow so need to speed up
                left = mp +1 
        
        return left
                