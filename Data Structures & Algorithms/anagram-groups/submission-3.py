class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        outputlst = []

        for i in strs: 
            if "".join(sorted(i)) not in hashmap: 
                hashmap["".join(sorted(i))] = [i]
            elif "".join(sorted(i)) in hashmap:
                 hashmap["".join(sorted(i))].append(i)

        for i in hashmap.values():
            outputlst.append(i)
    
        return outputlst

        