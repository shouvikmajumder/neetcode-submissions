class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        nums.sort()

        for num in nums:
            if num + 1 not in num_set and num + 1>0: 
                return num + 1
        
