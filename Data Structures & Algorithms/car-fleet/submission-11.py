class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_mappings = {}

        for idx in range(len(position)): 
            car_pos = position[idx]
            car_time = (target - position[idx]) / speed[idx]
            
            car_mappings[car_pos] = car_time

        stack = [position[0]]

        for pos in position: 
            
            if stack and car_mappings[stack[-1]] < car_mappings[pos]:
                stack.append(pos)
        
        return len(stack)