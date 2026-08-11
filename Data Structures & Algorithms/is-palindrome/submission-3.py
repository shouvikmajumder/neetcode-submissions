class Solution:
    def isPalindrome(self, s: str) -> bool:
        newlist = []

        for i in s:
            if i.isalpha():
                newlist.append(i.lower())
            if i.isdigit():
                newlist.append(i)
            
        return newlist == newlist[::-1]
