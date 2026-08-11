class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substr_set = set()

        left_ptr = 0

        max_counter = 0
        curr_counter  = 0

        for right_ptr in range(len(s)):
            
            character = s[right_ptr]

            while character in substr_set: 
                curr_counter -= 1
                substr_set.remove(s[left_ptr])
                left_ptr += 1

            if character not in substr_set: 
                substr_set.add(character) 
                curr_counter += 1

            max_counter = max(max_counter,curr_counter)

        max_counter = max(max_counter,curr_counter)
        return max_counter
                 
                     
