class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{","]":"[",")":"("}
        stack = []
        
        for i in s: 
            index = len(stack)
            stack.append(i)
            if i in hashmap:
                if hashmap[i] == stack[index-1]:
                    stack.pop()
                    stack.pop()
        return stack ==[]
        

                
            


            
