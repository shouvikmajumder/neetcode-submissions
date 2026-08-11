class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        left = 0

        key_freq = {}

        for right in range(len(s)):
            if s[right] not in key_freq:
                key_freq[s[right]] = 0
            key_freq[s[right]] += 1

            window_length = right - left + 1
            max_key = max(key_freq.values())

            while k < window_length - max_key:
                key_freq[s[left]] -= 1
                
                left += 1
                window_length = right - left + 1
                res = max(res, window_length)
            res = max(res, window_length)
        return res
