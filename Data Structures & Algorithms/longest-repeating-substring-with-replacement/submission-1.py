class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq_table = {}
        res = 0
        left = 0

        for right in range(len(s)):
        
            if s[right] not in freq_table:
                freq_table[s[right]] = 1
            elif s[right] in freq_table:
                freq_table[s[right]] += 1
            
            max_freq = max(freq_table.values())
            str_window = right - left + 1

            while str_window - max_freq > k : #this means that there is not enough to replace
                if s[left] in freq_table:
                    freq_table[s[left]] -= 1 
                    left += 1
                    max_freq = max(freq_table.values())
                    str_window = right - left + 1


            res = max(res, str_window)

        return res


        

        