class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        car_locations = {}

        for index in range(len(position)):
            car_locations[position[index]] = int((target - position[index]) / speed[index])

        position = sorted(position)[:: -1]

        stack = [[position[0],car_locations[position[0]]]]
        
        if len(position) < 1: 
            return len(stack)
        else: 
            
            for index in range(1,len(position)):
            
                car = position[index]
                
                stack_time = stack[-1][1]
                print(stack_time)

                curr_time = car_locations[car]
                print(curr_time)
            

                if curr_time > stack_time: 
                    stack.append([car, car_locations[car]])
        return len(stack)                