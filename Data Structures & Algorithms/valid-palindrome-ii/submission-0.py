class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        missahapps = 0 

        left,right = 0,len(s) -1

        while left <= right:
            
            if s[left] != s[right]: 
                if missahapps == 1: 
                    return False
                missahapps += 1
                left += 1 
                right -= 1
            else: 
                left += 1
                right -= 1         

        return True