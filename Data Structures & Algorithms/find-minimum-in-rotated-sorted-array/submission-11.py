class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0 , len(nums) -1 

        while left < right: 
            mp = (left + right) // 2

            if nums[mp] > nums[right]:
                left = mp + 1
            else:
                right = mp 
        return nums[left]

# [1,2,3,4,5,6]

'''
[4,5,6,1,2,3]
4 6 3
1 2 3



'''