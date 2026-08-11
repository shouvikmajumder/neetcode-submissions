class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        out = []

        hashmap = {}

        for i in nums: 
            if i not in hashmap: 
                hashmap[i] = 1
            elif i in hashmap:
                hashmap[i] += 1
        
        vallst = sorted(hashmap.values())[::-1][:k]

        for key in hashmap: 
            if hashmap[key] in vallst:
                out.append(key)
                
        return out
        
        