class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
            have the first word be the prefix

            iterate through every character in the word and compare it amongst the rest of the characters 
            in the array

            while doing this we need to keep track of the build string, if there is a discrepancy 
            we return res immediately

        ''' 
        prefix = strs[0]

        for words in strs[1:]:
            j = 0
            while j < min(len(prefix),len(words)):
                if prefix[j] != words[j]:  
                    break
                j += 1
            prefix = prefix[:j]
        
        return prefix

