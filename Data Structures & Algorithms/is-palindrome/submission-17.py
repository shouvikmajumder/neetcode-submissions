class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        build_str = ""

        for i in s: 
            if i.isalpha():
                build_str += i.lower()
            elif i.isdigit():
                build_str += i

        
        left,right = 0, len(build_str) -1 

        while left <= right:
            if build_str[left] != build_str[right]:
                return False
            left +=1 
            right -=1 
        return True