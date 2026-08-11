class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left, right = 0, len(nums) - 1 

        
        while(left <= right):
            
            mp = (left + right) // 2

            if nums[mp] == target:
                return mp
                
            elif nums[mp] > target:
                right = mp - 1  
            elif nums[mp] < target:
                left = mp + 1
        
        return -1 
            

