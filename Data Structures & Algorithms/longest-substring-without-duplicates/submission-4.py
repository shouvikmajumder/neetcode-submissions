class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abcdc



        if s == "":
            return 0
        elif len(s) == 1:
            return 1
        else: 
            checkstr= ""
            lst = []
            l,r = 0,1
            checkstr += s[l]
            while(r<len(s)):
                if s[r] not in checkstr: 
                    checkstr += s[r]
                    print(checkstr)
                    r +=1 
                elif s[r] in checkstr: 
                    lst.append(int(len(checkstr)))
                    checkstr = ""
                    l +=1
            lst.append(len(checkstr))
            return max(lst)

