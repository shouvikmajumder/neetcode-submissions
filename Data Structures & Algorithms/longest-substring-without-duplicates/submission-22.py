class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substrset = set()

        left = 0 

        max_substr = 0
        for right in range(len(s)):
            print(substrset)
    
            if s[right] in substrset: 
                substrset.remove(s[left])
                left += 1 
            
            substrset.add(s[right])
            
            max_substr = max(max_substr, len(substrset))
        
        max_substr = max(max_substr, len(substrset))
        return max_substr