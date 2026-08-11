class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(set(nums))

        out = []
        lst = []

        for i in range(len(nums)):
            if i == 0: 
                lst.append(nums[i])
            
            elif nums[i] == nums[i-1] + 1:
                lst.append(nums[i])
                
            else:
                out.append(lst)
                lst = [nums[i]]

        out.append(lst)
        max_len = 0

        for i in out:
            max_len = max(max_len, len(i))

        return max_len 
        

            
            

        