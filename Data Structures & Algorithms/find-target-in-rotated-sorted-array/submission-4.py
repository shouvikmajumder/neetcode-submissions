class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left, right = 0, len(nums) - 1

        #  1 2 3 4 5 6 7 8   target = 2
        #  8 1 2 3 4 5 6 7


        while(left <= right):
            mid_point = (left + right) // 2

            if nums[mid_point] == target: 
                return mid_point

            if target in nums[left:mid_point]:
                right = mid_point
            elif target in nums[mid_point:]: 
                left = mid_point + 1 
            else:
                return -1 


            
            