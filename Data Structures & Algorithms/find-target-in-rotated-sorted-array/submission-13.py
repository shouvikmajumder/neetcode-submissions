class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left <= right: 
            
            mp = (left + right) //2 

            if nums[mp] == target: 
                return mp
            
            elif nums[mp] <= nums[right]: #sorted
                if nums[mp] <= target <= nums[right]:
                    left = mp
                else: 
                    right = mp - 1
            elif nums[left] <= nums[mp]:
                if nums[left] <= target <= nums[mp]:
                    right = mp
                else:
                     left = mp + 1
            else: 
                return -1
        return -1

