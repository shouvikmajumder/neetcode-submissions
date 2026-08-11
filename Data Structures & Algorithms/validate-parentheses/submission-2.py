class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{","]":"[",")":"("}
        stack = []
        
        for i in s: 
            index = len(stack)
            stack.append(i)
            if i in hashmap:
                if index>0 and stack[index - 1] == hashmap[i]:
                    stack.pop()
                    stack.pop()
        
        return stack == []




        
        