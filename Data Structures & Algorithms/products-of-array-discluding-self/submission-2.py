class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        output = [0] * len(nums)

        for i in range(len(nums)):
            prod = 1 
            
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    continue
                prod *= nums[j]
            
            output[i] = prod

        return output