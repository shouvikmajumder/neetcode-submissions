class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        outputlst = []
        for i in strs:
            x = ",".join(sorted(i))
            if x not in check:
                check[x] = [i]
            elif x in check:
                check[x].append(i)
    
        for i in list(check.values()):
            outputlst.append(i)
        return outputlst    
            