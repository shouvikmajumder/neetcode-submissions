class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ["+","-","*","/"]

        stack = []

        for i in tokens:
            if i not in operator:
                stack.append(i)
            if i in operator: 
                x = stack.pop()
                y = stack.pop()

                if i == "+":
                    stack.append(int(x)+int(y))
                elif i == "-":
                    stack.append(int(y)-int(x))
                elif i == "*":
                    stack.append(int(x)*int(y))
                elif i == "/":
                    stack.append(int(y)/int(x))
        return int(stack.pop())
                

                

        