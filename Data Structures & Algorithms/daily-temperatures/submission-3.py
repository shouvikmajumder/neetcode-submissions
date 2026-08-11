class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output_arr = [0] * len(temperatures) 

        stack = [[0, temperatures[0]]] #index,value

        for index in range(1,(len(temperatures))):
            
            current_temp = temperatures[index]

            while stack and stack[-1][1] < current_temp: 
                output_arr[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            print(output_arr)
            
            stack.append([index, current_temp])

        return output_arr            



        