class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        count = len(s)

        for i in range(count):
            if s[i] != t[i]:
                return t[i]
        return t[-1]