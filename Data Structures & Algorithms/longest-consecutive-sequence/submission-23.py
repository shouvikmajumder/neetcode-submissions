class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        max_length = 0
        for num in num_set: 

            if (num - 1) not in num_set:
                #beginning of a new sequence
                curr_len = 1 
                curr_num = num

                while (curr_num + 1) in num_set: 
                    curr_len += 1
                    curr_num += 1
                                
                max_length = max(max_length,curr_len)

        return max_length