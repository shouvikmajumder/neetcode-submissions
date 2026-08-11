class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        substr_set = set()
        
        left = 0
        max_counter = 0
        curr_counter = 0

        for right in range(len(s)):
            character = s[right]
            if character not in substr_set: 
                substr_set.add(character)
                curr_counter += 1
            elif character in substr_set: 
                max_counter = max(max_counter, curr_counter)
                curr_counter = 0  
                while character in substr_set: 
                    substr_set.remove(character)
                    left += 1
        max_counter = max(max_counter, curr_counter)

        return max_counter
         

