class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for i in strs:
            if " ".join(sorted(i)) in hashmap: 
                hashmap[" ".join(sorted(i))].append(i)
            elif " ".join(sorted(i)) not in hashmap: 
                hashmap[" ".join(sorted(i))]  = [i]

        return list(hashmap.values())        
       