class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for i in s:
            if i not in hash1:
                hash1[i] = 0
            elif i in hash1:
                hash1[i] +=1 
        
        for i in t:
            if i not in hash2:
                hash2[i] = 0
            elif i in hash2:
                hash2[i] +=1 
        
        return hash1 == hash2
        
            
                
        