class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        count = len(t)

        for i in range(len(t) -1 ):
            if s[i] != t[i]:
                return t[i]
        return t[-1]