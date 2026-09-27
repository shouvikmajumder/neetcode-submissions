class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        num_mappings = {}

        for num in nums:
            if num not in num_mappings: 
                num_mappings[num] = 1 
            else:
                num_mappings[num] += 1
        
        for key in num_mappings: 
            if num_mappings[key] >(len(nums)//2):
                return key
        