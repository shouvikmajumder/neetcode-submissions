class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        parent_dict = {"}": "{","]": "[", ")":"("}

        for i in s: 
            stack.append(i)

            stack_index = len(stack) - 1

            if i in parent_dict:
                print("hello")
                if stack[stack_index - 1] == parent_dict[i]:
                    stack.pop()
                    stack.pop()
        
        return stack == []