class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_tracker = {}

        left_ptr = 0

        longest_substr = 0

        for right_ptr in range(len(s)):

            if s[right_ptr] not in char_tracker: 
                char_tracker[s[right_ptr]] = 0
            char_tracker[s[right_ptr]] += 1


            max_key_val = max(char_tracker.values())

            print(right_ptr, left_ptr)

            window_length = (right_ptr - left_ptr) + 1

            while (window_length - max_key_val) > k :
                char_tracker[s[left_ptr]] -= 1  
                left_ptr += 1
                window_length = (right_ptr - left_ptr) + 1

            longest_substr = max(longest_substr, window_length)

        return longest_substr