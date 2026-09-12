class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_size_subarr = 100000
        left = 0
        total = 0
        for right in range(len(nums)): 
            
            while total > target:
                total -= nums[left]
                window = right - left 
                print(window)
                min_size_subarr = min(min_size_subarr,window)
                left += 1
            total += nums[right]
        
        if min_size_subarr == 100000:
            return 0
        return min_size_subarr