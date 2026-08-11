class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) -1 

        while left < right: 

            mp = (left + right) //2

            # need to find which side is sorted

            if nums[mp] < nums[right]:
                # min should be in here in that case
                right = mp
            else: 
                left = mp + 1
        return nums[left]
