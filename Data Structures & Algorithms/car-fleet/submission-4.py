class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        car_fleet_mappings = {} 

        for i in range(len(position)): 
            car_fleet_mappings[position[i]] = speed[i]


        position_sorted = sorted(car_fleet_mappings)[::-1]
        
        # 0 1 4 7 target = 10
        # 10 9 5 3 --> 3 5 9 10
        stack = []
        output = []
        
        for i in range(len(position_sorted)):

            distance = target - position_sorted[i]
            time = distance / (car_fleet_mappings[position_sorted[i]]) # this is the speed at the position 

            if stack == []:
                stack.append(time)
            else: 
                if stack[-1] < time:
                    output.append(stack.pop())
                    stack.append(time)
        if stack != []:
            output.append(stack.pop())

        return len(output)
        
                
                     
    



            
        return len(output)
        


       
    

