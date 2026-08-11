class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        car_locations = {}

        for index in range(len(position)):
            car_locations[position[index]] = ((target - position[index]) / speed[index])

        

        position = sorted(position)[:: -1]

        for i in position: 
            temp = [i,car_locations[i]]
            print(temp)
        

        stack = [[position[0],car_locations[position[0]]]]
        
        if len(position) <= 1: 
            return len(stack)
        else: 
            
            for index in range(1,len(position)):
            
                car = position[index]
                
                stack_time = stack[-1][1]

                curr_time = car_locations[car]
            
                if curr_time > stack_time: 
                    stack.append([car, car_locations[car]])

        return len(stack)                