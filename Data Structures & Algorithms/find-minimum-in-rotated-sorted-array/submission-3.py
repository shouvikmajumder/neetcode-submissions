class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) -1 

        # 3 4 5 6 1 2
        # 1 2 3 4 5 6

        while(left <= right):
            mid_point = (left + right)// 2

            # need to find the pivot

            if nums[mid_point] > nums[right]:
                # pivot found
                left = mid_point + 1 
        
            elif nums[mid_point] < nums[left]:
                #pivot found
                left = mid_point
            else:
                right = mid_point -1 
        return nums[mid_point]

    
            





            



            

                


            

              
        



            
            

            