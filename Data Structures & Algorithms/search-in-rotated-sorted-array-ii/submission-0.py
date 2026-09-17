class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left,right = 0, len(nums) - 1
        while left < right: 
            midp = (left + right) //2 
            print(nums[midp])
            if nums[midp] == target: 
                return True 
            elif nums[left] < nums[midp]:
                if nums[left] <= target < nums[midp]:
                    right = midp
                else: 
                    left = midp + 1 
            else:
                if nums[midp] < target <= nums[right]:
                    left = midp + 1 
                else: 
                    right = midp
        return False 