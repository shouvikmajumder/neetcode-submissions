class Solution:
    def isPalindrome(self, s: str) -> bool:
        newlist = []
        for i in s:
            if i.isalpha():
                newlist.append(i.lower())
        return newlist[::-1] == newlist