class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) -1 

        # 3 4 5 6 1 2

        while(left <= right):
            mid_point = (left + right)// 2

            # need to find the pivot
            if nums[left] > nums[mid_point]: 
                # its in the left half therefore 
                right = mid_point 
            else:
                # pivot is in the rigth half
                left = mid_point + 1
            
        return nums[mid_point]





            



            

                


            

              
        



            
            

            