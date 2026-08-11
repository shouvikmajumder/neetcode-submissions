class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False 
        
        left, right = 0, len(s1)-1 

        while right <= len(s2) -1 : 
            if sorted(s2[left:right+1]) == sorted(s1):
                return True
            
            left += 1 
            right += 1
        
        return False
        
