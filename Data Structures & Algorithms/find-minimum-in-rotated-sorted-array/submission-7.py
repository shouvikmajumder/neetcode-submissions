class Solution:
    def findMin(self, nums: List[int]) -> int: 
        
        left, right = 0, len(nums) -1 

        while left < right: 

            mid_p = (left + right) // 2 

            if nums[mid_p] > nums[right]:
                left = mid_p + 1
            else:
                right = mid_p
        
        return nums[left]    
                 
