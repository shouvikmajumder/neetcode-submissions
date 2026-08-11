class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        x = self.createhash(s)
        y = self.createhash(t)
        return x == y
        
    def createhash(self, z: str) -> dict:
        hashmap = {}
        for i in z: 
            if i not in hashmap: 
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        return hashmap


        
        