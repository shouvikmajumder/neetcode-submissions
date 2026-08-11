class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for i in strs: 
            word = "".join(sorted(i))
            if word not in hashmap: 
                hashmap[word] = [i]
            elif word in hashmap: 
                hashmap[word].append(i)
        
        return list(hashmap.values())
            
            