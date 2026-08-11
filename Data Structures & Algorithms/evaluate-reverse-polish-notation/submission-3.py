class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oplst = ["+","-","/","*"]
        stack = []

        for token in tokens:
            if token in oplst: 
                x = int(stack.pop())
                y = int(stack.pop())
                if token == "+":
                    stack.append(int(x + y))
                elif token == "*":
                    stack.append(int(x * y))
                elif token == "-":
                    stack.append(int(y - x))
                elif token == "/":
                    stack.append(int(y / x))
            else:
                stack.append(token)
        return stack[0]
