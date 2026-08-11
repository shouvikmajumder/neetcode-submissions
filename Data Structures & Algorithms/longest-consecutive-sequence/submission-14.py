class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = sorted(list(set(nums)))

        if len(nums) < 1: 
            return 0

        left,right = 0,1

        max_conseq_counter = 1
        
        max_count_out = 1
        

        while (right < len(nums)):
            
            if nums[left] + 1 == nums[right]:
                # seq
                max_conseq_counter += 1 
                left +=1 
                right += 1 
            
            elif nums[left] + 1 != nums[right]:
                max_count_out = max(max_count_out,max_conseq_counter)
                max_conseq_counter = 1
                left = right
                right += 1 
        return max(max_count_out,max_conseq_counter)


            


