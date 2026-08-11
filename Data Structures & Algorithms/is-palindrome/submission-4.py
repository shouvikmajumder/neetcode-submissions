class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s[-1].isalpha() == False :
            s = s[:-1]
        else: 
            x = 0 
            y = len(s)-1

            while(x<=len(s)-1):
                if(s[x]!=s[y]):
                    return False
                x+= 1
                y-=1
        return True
            
