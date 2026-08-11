class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        nums = set(nums)
        nums = list(nums)

        if len(nums) == 0:
            return 0
        
        left = 0
        conseq = 1
        conseq_out = 1
        
        nums.sort()
        
        for right in range(1,len(nums)): 
            
            if nums[left] + 1 != nums[right]:
                conseq = 1
                left += 1 
            elif nums[left] + 1 == nums[right]:
                print("this statement reached")
                conseq +=1 
                left += 1
            conseq_out = max(conseq_out,conseq)
        
        return conseq_out



            

        