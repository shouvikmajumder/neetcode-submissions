class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            elif i in hashmap:
                hashmap[i] +=1 
        for i in hashmap:
            if hashmap[i] == 1:
                return i    