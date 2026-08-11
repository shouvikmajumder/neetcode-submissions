class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1

        check = 0

        while(l<r):
            area = min(heights[l],heights[r]) * (r-l)
            
            if area > check:
                check = area
            elif min(heights[l+1],heights[r]) * (r-(l+1)) > check: 
                l +=1
            elif min(heights[l],heights[r-1]) *((r-1)-(l)) > check: 
                r -= 1
            else:
                l +=1
                r -= 1 

        return check 
            
            

           
            