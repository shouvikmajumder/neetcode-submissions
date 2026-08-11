class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oplst = ['*', '-', '+', '/']

        for i in tokens:
            if i not in oplst:
                stack.append(i)
            if i in oplst:
                if i == "*":
                    x= stack.pop()
                    y =stack.pop()
                    stack.append(int(x)*int(y))
                if i == "-":
                    x= stack.pop()
                    y =stack.pop()
                    stack.append(int(y)-int(x))
                if i == "/":
                    x= stack.pop()
                    y =stack.pop()
                    stack.append(int(y)/int(x))
                if i == "+":
                    x= stack.pop()
                    y =stack.pop()
                    stack.append(int(x)+int(y))
        return int(stack.pop())
                