class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        temp_stack = [] # [temp, index]

        for i in range(len(temperatures)):

            while temp_stack != [] and temperatures[i] > temp_stack[-1][0]:

                temp_stack_obj = temp_stack.pop()
                
                stack_temp = temp_stack_obj[0]
                stack_index = temp_stack_obj[1]
                
                res[stack_index] = i - stack_index

            temp_stack.append([temperatures[i], i])
        
        return res 




            