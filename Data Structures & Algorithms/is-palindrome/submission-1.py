class Solution:
    def isPalindrome(self, s: str) -> bool:
        newlist = []
        for i in s:
            if i.isalpha():
                newlist.append(i.lower())
            elif isinstance(i,int):
                newlist.append(i)
        return newlist[::-1] == newlist