class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        topk = []
        
        for i in nums:
            if i not in hashmap:
                hashmap[i]= 1
            elif i in hashmap:
                hashmap[i]+=1 
        
        for key in hashmap:
            if hashmap[key] >= k:
                topk.append(key)
        return topk
        