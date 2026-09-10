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

        stack = [asteroids[0]]

        for index in range(1, len(asteroids)):
            curr_ast = asteroids[index]
            prev_ast = stack[-1]
            #Conditions
            #same direction
            if (curr_ast < 0 and prev_ast > 0) or (curr_ast > 0 and prev_ast < 0):
                if abs(curr_ast) != abs(prev_ast):
                    max_val_ast = max(abs(curr_ast),abs(prev_ast))
                    if abs(curr_ast) == max_val_ast: 
                        stack.pop()
                        stack.append(curr_ast)
                elif abs(curr_ast) == abs(prev_ast):
                    stack.pop()
                    continue
            else: 

                stack.append(curr_ast)
            print(stack)

        return stack

