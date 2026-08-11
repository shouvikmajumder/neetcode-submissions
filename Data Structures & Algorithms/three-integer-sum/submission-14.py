class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        outputarr = []

        nums.sort()

        
        for index in range(len(nums)):

            left,right = index + 1 , len(nums) - 1

            while left < right: 
                if nums[index] + nums[left] + nums[right] == 0:
                    sublst = [nums[index],nums[left],nums[right]]
                    sublst.sort()
                    if sublst not in outputarr:
                        outputarr.append(sublst)
                    left += 1
                    right -= 1 
                
                elif nums[index] + nums[left] + nums[right] > 0:
                    right -=1 
                elif nums[index] + nums[left] + nums[right] < 0:
                    left += 1 
        
        return outputarr
            

        