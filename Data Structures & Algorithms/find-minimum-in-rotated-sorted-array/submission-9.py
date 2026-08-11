class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            Problem Approach: 

                Just take a look at the right side, a clear giveaway is that
                if the right is smaller than the mid_point, it is going to 
                garuntee that it contains the smallest

                All you have to do is check the rightside 
        '''


        left, right = 0, len(nums) - 1 

        while left < right: 
            midpoint = (left + right) // 2

            if nums[midpoint] > nums[right]: 
                #garuntees the min 
                left = midpoint + 1 
            else:   
                right = midpoint
        return nums[left]

    # [5,6,0,1,2,3,4]