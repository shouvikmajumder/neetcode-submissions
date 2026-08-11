class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums: 
            if i not in hashmap:
                hashmap[i] = 1
            elif i in hashmap:
                hashmap[i]+=1


        searchlst = sorted(hashmap.values())[::-1][:k]        
        out = []

        for i in hashmap: 
            if hashmap[i] in searchlst: 
                out.append(i)

        return out