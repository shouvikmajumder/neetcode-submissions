class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ptr_lst = []

        right = 0
        output = 0
        
        while(right < len(s)):
            
            if s[right] in ptr_lst:
                output = max(output,len(ptr_lst))
                ptr_lst = ptr_lst[1:]
            elif  s[right] not in ptr_lst: 
                ptr_lst.append(s[right])
            right += 1
            
        return output



