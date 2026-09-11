class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
            Objective: Find out state of asteroids after all collisions
            The abs val is the size and sign is the direction 

            Conditions: 
                IF 2 asteroids meet smaller one will explode
                IF both the same size and same direction both explode
                both are the same direction nothing happens
        '''
        stack = []

        for a in asteroids: 
            
            while stack and a < 0 and stack[-1] > 0:
                diff = stack[-1] + a 
                if diff < 0: 
                    stack.pop()   
                elif diff > 0:
                    a = 0
                    break
                elif diff == 0: 
                    a = 0
                    stack.pop()
                    break 
            if a != 0: 
                stack.append(a)

        return stack