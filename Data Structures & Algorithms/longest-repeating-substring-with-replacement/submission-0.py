class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        res = 0
        char_freq = {}

        for right in range(len(s)):
            if s[right] not in char_freq:
                char_freq[s[right]] = 1
            elif s[right] in char_freq:
                char_freq[s[right]] += 1

            window = right - left + 1 
            max_freq = max(char_freq.values())

            while(window - max_freq > k):
                char_freq[s[left]] -= 1
                left += 1
                window = right - left + 1
                max_freq = max(char_freq.values())
                

            res = max(res,window)

        return res


            
            


        

            