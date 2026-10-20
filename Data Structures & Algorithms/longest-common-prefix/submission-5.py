class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            curr_word = strs[i]
            idx = 0
            
            while idx < min(len(curr_word),len(prefix)): 
                if prefix[idx] != curr_word[idx]:
                    break
                idx += 1                 
            prefix = prefix[:idx]

        return prefix
            