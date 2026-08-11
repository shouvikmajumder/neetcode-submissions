class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashfunc = {}

        for i,j in enumerate(nums):
            difference = target - j
            if difference in hashfunc:
                return [hashfunc[difference],i]
            else:
                hashfunc[j] = i
        