from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        output = [0] * len(nums)

        for i in range(len(nums)):
            output[i] = prod(nums[:i]) * prod(nums[i+1:])
        return output
