class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_counter = {}
        longest_window = 0
        window = 0
        left = 0 

        for right in range(len(s)):
            
            if s[right] not in char_counter: 
                char_counter[s[right]] = 1 
            elif s[right] in char_counter: 
                char_counter[s[right]] += 1 
            
            max_key_val = max(char_counter.values())
            window_length = (right - left) + 1

            while (window_length - max_key_val) > k: 
                char_counter[s[left]] -= 1
                left += 1
                window_length  = right - left + 1
                max_key_val = max(char_counter.values())

            longest_window = max(longest_window, window_length)
        return longest_window    



