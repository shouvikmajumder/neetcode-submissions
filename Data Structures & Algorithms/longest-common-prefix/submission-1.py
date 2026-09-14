class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1,len(strs)): 
            j = 0
            current_word = strs[i]
            while j < min(len(prefix),len(current_word)):
                
                if prefix[j] != current_word[j]:
                    break
                    
                j += 1
            prefix = prefix[:j]

        return prefix

