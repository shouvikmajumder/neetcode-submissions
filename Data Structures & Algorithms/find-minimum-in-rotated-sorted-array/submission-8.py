class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        '''
            Problem Approach: 
                We are going to implement a binary search

                typically if an array is not rotated left < mid < right

                however since it is not rotated:
                if mid > right: this would indicate that the smallest number would be
                in the right most region
                    This is where you would progress the left pointer to the midpoint
                
                if left > mid, then there is a clear indication that the left 
                region has the lowest value
        '''         

        left, right = 0 , len(nums) - 1

        while left < right: 
            midpoint = (left + right) // 2

            if nums[midpoint] < nums[left]: 
                right = midpoint #midpoint could be the smallest value
            else: 
                left = midpoint + 1 
        return nums[left]

