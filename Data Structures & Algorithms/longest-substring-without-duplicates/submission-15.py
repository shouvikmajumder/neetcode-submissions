class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique_lst = set()
        left = 0
        output = 0

        for right in range(len(s)):
            
            if s[right] in unique_lst: 
                while (left<right):
                    unique_lst.remove(s[left])
                    left += 1
        
            unique_lst.add(s[right])
            output = max(output, (right - left) + 1)
        
        return output
