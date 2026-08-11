class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        char_freq = {}
        left = 0
        res = 0 

        for right in range(len(s)):
            if s[right] not in char_freq:
                char_freq[s[right]] = 0
            char_freq[s[right]] += 1

            #freq table updates every itr

            max_key_val= max(char_freq.values())

            window_length = right - left + 1

            while window_length - max_key_val > k: 
                char_freq[s[left]] -= 1
                left += 1
                window_length = right - left + 1
                max_key_val= max(char_freq.values())
            res = max(res,window_length)
        
        return res
                

            

        

