class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        if len(word1) != len(word2): 
            for index in range(min(len(word1), len(word2))): 
                res += word1[index]
                res += word2[index]
            if len(word1)> len(word2): 
                res += word1[len(word2):]
            else: 
                res += word2[len(word1):]
        
        else: 
            for index in range(len(word1)): 
                res += word1[index]
                res += word2[index]
        return res