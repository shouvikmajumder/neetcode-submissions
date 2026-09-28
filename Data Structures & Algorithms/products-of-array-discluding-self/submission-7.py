class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)    

        prefix_prod = 1 

        for idx in range(len(nums)):
            prefix[idx] = prefix_prod
            prefix_prod *= nums[idx]

        suffix_prod = 1 
        for idx in range(len(nums)-1, -1, -1): 
            suffix[idx] = suffix_prod
            suffix_prod *= nums[idx]

        return [suffix[idx] * prefix[idx] for idx in range(len(nums))]     