class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:
            if op == "+": 
                newval = sum(stack)
                stack.append(newval)
            elif op == "C":
                stack.pop()
            elif op == "D": 
                prev = stack[-1]
                stack.append(prev * 2)
            else:
                stack.append(int(op))
        return sum(stack)