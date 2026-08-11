class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ending_position = []

        
        for pos in position: 
            ending_position.append(target - pos)

        cars_dict = {}

        for index in range(len(speed)): 
            #end pos : time
            cars_dict[ending_position[index]] = ending_position[index]/speed[index] #time is the value here

        #last place to first
        sorted_car_pos = sorted(cars_dict)

        stack = []

        for car in sorted_car_pos: 
            time = cars_dict[car]

            if stack and stack[-1] >= time: 
                continue
            stack.append(time)
        return len(stack)