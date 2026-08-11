class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left <= right: 
            
            mp = (left + right) //2 

            if nums[mp] == target: 
                return mp
            
            elif nums[mp] < nums[right]: #sorted
                if target in nums[mp:]:
                    left = mp
                else: 
                    right = mp - 1
            elif nums[left] < nums[mp]:
                if target in nums[left:mp +1]:
                    right = mp
                else:
                     left = mp + 1
            else: 
                return -1
            

