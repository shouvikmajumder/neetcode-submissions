class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            Problem Approach/Notes: 
                
                What exactly is a rotation? 
                    A rotation is bascially the number of elements you are moving to the front of the array
                        - keep in mind that this is already sorted
                
                We know that the algorithm wants a O(logn) solution, which means that it is going to use a 
                binary search algo

        '''        

        left,right = 0, len(nums) - 1

        # we want to find the min 

        while left < right:     
            
            midpoint = (left + right) //2 
            
            if nums[midpoint] > nums[right]: 
                # the right region is going to contain the smallest value 
                left = midpoint + 1 
            else: 
                # this would mean that the left side value contains the lowest 
                right = midpoint 
        
        return nums[left]
            



            

                
            




