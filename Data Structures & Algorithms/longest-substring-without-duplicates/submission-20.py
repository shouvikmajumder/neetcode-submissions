class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        uniquq_lst = []
        left = 0
        output = 0

        for right in range(len(s)):
            
            if s[right] in uniquq_lst: 
                while s[right] in uniquq_lst:
                    uniquq_lst.remove(s[left])
                    left += 1
            uniquq_lst.append(s[right])
            output = max(output, right - left + 1)
        
        return output
        