class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        # unique num as key and val is the num of occurances
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            elif i in hashmap:
                hashmap[i] += 1

        vals = list(sorted(hashmap.values()))[::-1][:k]
        outputlst = []

        for i in hashmap: 
            if hashmap[i] in vals:
                outputlst.append(i)
        return outputlst
                