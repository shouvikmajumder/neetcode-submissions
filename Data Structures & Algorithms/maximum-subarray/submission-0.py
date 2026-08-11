class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        running_best = nums[0]

        for window_size in range(len(nums)):

            left, right = 0, window_size

            while (right < len(nums)): 
                running_best = max(running_best, sum(nums[left:right + 1]))
                left +=1 
                right += 1

        return running_best
