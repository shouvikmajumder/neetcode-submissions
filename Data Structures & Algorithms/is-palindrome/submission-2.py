class Solution:
    def isPalindrome(self, s: str) -> bool:
        newlist = []
        for i in s:
            if i.isalpha():
                newlist.append(i.lower())
            elif isinstance(i,int):
                return False
                
        return newlist[::-1] == newlist