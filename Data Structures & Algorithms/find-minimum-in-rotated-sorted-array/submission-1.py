class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0 , len(nums) - 1

        while(left<=right):
            mid_point = (left + right)//2

            if nums[mid_point] == min(nums[mid_point],nums[left],nums[right]):
                return nums[mid_point]

            elif nums[left] < nums[right]:
                right = mid_point  - 1
            elif nums[right] < nums[left]:
                left = mid_point + 1
        