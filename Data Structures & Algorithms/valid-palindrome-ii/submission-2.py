class Solution:
    def validPalindrome(self, s: str) -> bool:

        left,right = 0,len(s) -1

        while left <= right:
            
            if s[left] != s[right]:
                # want to skip either right or left and check if its a palindrome 
                skipL = s[left + 1: right +1]
                skipR = s[left:right]

                return skipL == skipL[::-1] or skipR == skipR[::-1]
            left += 1
            right -=1 

        return True