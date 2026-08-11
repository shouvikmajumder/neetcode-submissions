class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0
        elif int(len(s)) == 1:
            return 1
        else:
            l,r = 0,1
            checkstr = ""
            lst = []

            while(r<len(s)):
                if checkstr == "":
                    checkstr += s[l]
                elif s[r] not in checkstr:
                    checkstr += s[r]
                    r += 1
                elif s[r] in checkstr:
                    lst.append(len(checkstr))
                    checkstr = ""
                    l = r 
                    r = l +1 


            return max(lst)
            