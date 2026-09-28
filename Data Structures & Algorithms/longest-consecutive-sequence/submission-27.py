class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_consecutive = 0
        
        for num in nums: 
            current_sequence = 1
            while num + 1 in nums_set: 
                current_sequence += 1 
                num += 1 
            
            longest_consecutive = max(longest_consecutive,current_sequence)
                
        
        return longest_consecutive