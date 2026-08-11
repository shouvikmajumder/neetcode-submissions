class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,j in enumerate(numbers):
            diff = target - j
            if diff in hashmap:
                return sorted([hashmap[diff]+1,i+1])
            hashmap[j] = i
