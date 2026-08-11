class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()

        for i in range(len(nums)):

            left, right = i + 1, len(nums)-1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    output.add((nums[i],nums[left],nums[right]))
                    left +=1 
                    right -=1 
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
            
    
        return list(output)