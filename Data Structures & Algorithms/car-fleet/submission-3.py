class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        stack = []
        
        for i in range(len(position)):
            hashmap[position[i]] = (target - position[i])/(speed[i])
        
        hashlst = sorted(list(hashmap.keys()))[::-1]
        print(hashlst)
        
        for i in range(len(hashlst)):
            stack_index = len(stack)
            
            if stack_index == 0: 
                stack.append(hashlst[i])
            else: 
                if hashmap[stack[-1]] < hashmap[hashlst[i]]:
                    stack.append(hashlst[i])
            
        return len(stack)          