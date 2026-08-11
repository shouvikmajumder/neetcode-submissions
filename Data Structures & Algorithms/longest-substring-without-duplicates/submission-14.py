class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(len(s))
        ptr_lst = []

        right = 0
        output = 0
        
        while(right < len(s)):

            if s[right] not in ptr_lst: 
                ptr_lst.append(s[right])
                output = max(output,len(ptr_lst))

            elif s[right] in ptr_lst:
                output = max(output,len(ptr_lst))
                ptr_lst = ptr_lst[1:]

            right += 1
        
        # print(ptr_lst)
        
            
        return output




