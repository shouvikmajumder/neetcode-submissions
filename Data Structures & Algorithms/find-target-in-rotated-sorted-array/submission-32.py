class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            Problem Approach/Notes: 
                
                Everytime we see O(log n) we know we are going to do some sort of binary search

                Algo idea : 
                    Since this array is rotated n times, we know that one of the regions 
                    is going to be in sorted order

                    The core idea is you are going to look throught the ranges and determine 
                    if target is in that range, if it is not, then you can just update
                    either the left of right pointer accordingly so that it is checking the 
                    other region 

                    Ideally, when you are searching, l,r,mp are going to converge to a single point
                    that point being the index of target
        '''
        
        left,right = 0, len(nums) - 1

        while left <= right:
            mp = (left + right) // 2

            if nums[mp] == target: 
                return mp 
            #Core logic (want to find the sorted range)
            if nums[mp] < nums[right]:
                if nums[mp] < target <= nums[right]: 
                    # this means that you want to move the left pointer to the right range
                    left = mp + 1 
                else: 
                    right = mp - 1
            
            # what happens if the right region is not sorted? 
            else: 
                # this condition is going to trigger if the right region is not sorted
                if nums[left] <= target < nums[mp]: 
                    right = mp - 1
                else: 
                    left = mp + 1 
                    
        return -1











