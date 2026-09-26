import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # we need a prefix array and a postfix array
        # mulitply both outpcomes into an ouput lst 

        prefix_lst = [1] * len(nums)
        suffix_lst = [1] * len(nums)

        output = [1] * len(nums)

        for i in range(len(nums)): 
            prefix_lst[i] = math.prod(nums[:i])
        
        index = len(nums) -1 

        while index >= 0: 
            suffix_lst[index] = math.prod(nums[index + 1:])
            index -= 1

        for i in range(len(nums)):
            output[i] = prefix_lst[i] * suffix_lst[i]

        return output