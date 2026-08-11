class Solution:
    def partition(self, s: str) -> List[List[str]]: 

        res = []
        part = []

        def backtrack(index): 
            if index > len(s) - 1: 
                res.append(part.copy())
                return
            #here you want to go through the index to the end of the str for substrs
            #you want to check if a substr is a paindrom before you add it to part
            #for exclusion you pop at the end 

            for j in range(index, len(s)):
                substr = s[index: j + 1]
                if self.isPali(substr): 
                    part.append(substr)
                    backtrack(j + 1)
                    part.pop()        
        backtrack(0)

        return res

    def isPali(self,arr):  
        return arr == arr[::-1]