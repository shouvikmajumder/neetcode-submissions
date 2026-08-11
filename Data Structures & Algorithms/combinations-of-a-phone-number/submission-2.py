class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
            Problem Apprach/Notes 
                We have to initally map every digit to the characters it represents 
                we can then create a backtrack function which is going to take in the builtstr and index as params

                base case that is good here is if the len(buildstr) == len(digits) since that means that we have
                completed our buildstr we can return out 

                If our basecase is not completed however, we would have to loop through the charaters that our 
                digits represents and add it to the buildstr 



        '''
        phone_book = { "2" :"abc", "3" :"def", "4" : "ghi", "5": "jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9" : "wxyz"}
        res = []

        def backtrack(index, curStr): 
            if len(curStr) == len(digits): 
                res.append(curStr)
                return 
            
            character = phone_book[digits[index]]

            for char in character: 
                backtrack(index + 1 , curStr +char)

        backtrack(0,"")
                
        if not digits: 
            return []

        return res
