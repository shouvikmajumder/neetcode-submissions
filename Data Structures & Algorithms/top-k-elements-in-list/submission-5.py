class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            elif i in hashmap:
                hashmap[i] +=1
                
        vals = list(sorted(hashmap.values())[::-1])[:k]

        outputlst = []
        for key in hashmap:
            if hashmap[key] in vals:
                outputlst.append(key)
        return outputlst[:k]

        
            