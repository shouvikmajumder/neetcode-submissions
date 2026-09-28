class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_consecutive = 0
        print(nums_set)
        for num in nums_set: 
            current_sequence = 1
            while num + current_sequence in nums_set: 
                current_sequence += 1 
            longest_consecutive = max(longest_consecutive,current_sequence)
        print(longest_consecutive)            

        return longest_consecutive