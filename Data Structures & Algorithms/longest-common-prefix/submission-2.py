class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            j = 0
            while j < min(len(word),len(prefix)): 
                print(prefix[j], word[j])
                if prefix[j] != word[j]:
                    break 
                j += 1

            prefix = prefix[:j]


        return prefix
            