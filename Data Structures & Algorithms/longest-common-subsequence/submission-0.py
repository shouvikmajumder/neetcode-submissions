class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1,text2 = sorted(text1),  sorted(text2)

        alpha = "abcdefghijklmnopqrstuvwxyz"
    
        print(text1,text2 )
        counter = 0

        new_str = ""

        for i in range(min(len(text1),len(text2))):
            if text1[i] in alpha and text2[i] in alpha:
                counter += 1 
        return counter