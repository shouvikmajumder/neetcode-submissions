class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for index in range(len(s)):

            if s[index] != "]":
                stack.append(s[index])

            else: 
                # extract inside bracket characters
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                # extract digits to its left
                stack.pop()

                digit_char = ""
                while stack and stack[-1].isdigit(): 
                    digit_char = stack.pop() + digit_char

                stack.append(substr * int(digit_char))
                
                

        return ("".join(stack))
                