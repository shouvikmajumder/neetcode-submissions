class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}
        
        for words in strs: 
            sorted_words = "".join(sorted(words))
            
            if sorted_words not in hashset: 
                hashset[sorted_words] = [words]
            elif sorted_words in hashset: 
                hashset[sorted_words].append(words)
        return list(hashset.values())
            
        

