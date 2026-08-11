class Solution:
    def findMin(self, nums: List[int]) -> int:

        #left,right,mp == same index 
        left, right = 0, len(nums) - 1 

        while left <= right: 
    
            mid_p = (left + right) // 2

            if nums[mid_p] > nums[right]:
                left = mid_p + 1 
            
            elif nums[left] > nums[mid_p]:
                right = mid_p
            else: 
                right = mid_p - 1 
                
        return nums[mid_p]  