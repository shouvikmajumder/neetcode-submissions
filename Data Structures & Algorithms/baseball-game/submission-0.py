class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:
            if op == "+":
                sum = 0
                for num in stack: 
                    sum += int(num)
                newval = str(sum)
                stack.append(newval)
            elif op == "D":
                val = stack.pop()
                newval = int(val) * 2 
                stack.append(val)
                stack.append(str(newval))
            elif op == "C":
                stack.pop()
            else:
                stack.append(op)

        res = 0

        for num in stack:
            res += int(num)

        return res