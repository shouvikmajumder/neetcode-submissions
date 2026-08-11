class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            Problem appoach: 

                Since you already know that you have n pairs, we can deduce that there will be
                exactly n left parenthesis and n right parenthesis 

                if both left and right equals to n that means that add a copy of the lst 
                that we have into res 
        '''

        res = []        

        def backtrack(Left, Right, sublst): 
            
            if Left == Right == n:
                res.append("".join(sublst.copy()))
                return
            if Left < n: 
                # need to generate the left side parenthesis
                sublst.append("(")
                backtrack(Left + 1, Right,sublst)
                sublst.pop() # This is the option of not including it  
            if Right< n:
                sublst.append(")")
                backtrack(Left, Right + 1,sublst)
                sublst.pop()
        backtrack(0,0,[])

        self.isValid(res[-1])

        output = []

        for combo in res:
            if self.isValid(combo):
                output.append(combo)

        return output

    def isValid(self, input_str):
        '''
            Want to traverse throught input str and if we run into an closed parenthesis we would just pop from the stack  
        ''' 
        stack = []

        for idx in range(len(input_str)):
            curr_char = input_str[idx]
            stack.append(curr_char)
            stack_idx = len(stack) - 1 
            
            if curr_char == ")" and stack[stack_idx - 1] == "(":
                stack.pop()
                stack.pop()

        return stack == []








