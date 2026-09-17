class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left,right = 0, len(nums) - 1
        while left <= right: 
            midp = left + (right - left) //2 

            if nums[midp] == target: 
                return True 
            if nums[left] < nums[midp]:
                if nums[left] <= target < nums[midp]:
                    right = midp - 1 
                else: 
                    left = midp + 1
            elif nums[left] > nums[midp]:
                if nums[midp] < target <= nums[right]:
                    left = midp + 1 
                else: 
                    right = midp - 1 
            else:
                left += 1 

        return False 