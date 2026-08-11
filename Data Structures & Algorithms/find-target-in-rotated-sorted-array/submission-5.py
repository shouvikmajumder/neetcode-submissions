class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left <= right: 
            mid_p = (left + right )// 2        
            if nums[mid_p] == target:
                return mid_p

            elif nums[mid_p] >= nums[left]: #left side is sorted
                if nums[left] <= target < nums[mid_p]: 
                    right = mid_p - 1
                else:
                    left = mid_p + 1
            else: #right side is sorted
                if nums[mid_p] < target <= nums[right]:
                    left = mid_p + 1
                else:
                    right = mid_p - 1

        return -1
