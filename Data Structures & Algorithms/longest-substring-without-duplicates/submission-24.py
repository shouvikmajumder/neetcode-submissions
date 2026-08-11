class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substrset = set()

        left = 0 

        max_substr = 0
        for right in range(len(s)):
    
            if s[right] in substrset: 
               
                while s[right] in substrset: 
                    substrset.remove(s[left])
                    left += 1 
            substrset.add(s[right])
            
            max_substr = max(max_substr, len(substrset))

        if len(substrset) > max_substr: 
            return len(substrset)

        return max_substr