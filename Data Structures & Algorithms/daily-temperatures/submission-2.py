class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        temp_init = len(temperatures) * [0] 

        stack = []

        for day in range(len(temperatures)):

            stack_item = [day,temperatures[day]]

            while stack and stack_item[1] > stack[-1][1]: 
                #current temp greater thatn prev 
                temp_init[ stack[-1][0]]= stack_item[0] - stack[-1][0]
                stack.pop()
            stack.append(stack_item)

        return temp_init

