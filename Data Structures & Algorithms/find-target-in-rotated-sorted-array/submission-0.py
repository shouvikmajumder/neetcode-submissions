class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left, right = 0, len(nums) - 1

        #  1 2 3 4 5 6 7 8 9  target = 2
        #  4 5 6 7 8 9 1 2 3  


        while(left <= right):
            mid_point = (left + right) // 2

            if nums[mid_point] == target: 
                return mid_point

            elif nums[left] < nums[mid_point]:
                # this is alreayd in sorted order
                if nums[left] < target and nums[mid_point]> target:
                    right = mid_point -1 
                else:
                    left = mid_point
            left = mid_point 
        return -1
                

            
            
            