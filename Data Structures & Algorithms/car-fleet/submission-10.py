class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            Problem Notes: 
            position [4,1,0,7] speed [2,2,1,1]
            
            Group the cars together, Target = 10 
            "Position:Speed" = {4:2, 1:2, 0:1, 7:1}

            Carfleet basically says a that car catches up to another car becomes a car fleet
            How can you check that car cathces up to anther car? 
                Ans time left: (target - position)/ speed to get the time 
            
            7,4,1,0
            stack = [7] curr time stack[-1] > curr append to stack 
            return len(stack)
        '''
        # create a mapping of the postions and the times 
        
        car_mappings = {}  
        stack = []
        # every element that gets appended to the stack is a different car fleet

        for i in range(len(position)): 
            car_mappings[position[i]] = (target - position[i])/speed[i]

        positions = list(car_mappings.keys())
        positions.sort()
        positions = positions[::-1]
        
        # iterate through positions and append to stack if the time of the current element is greater than
        # the time that is at the top of the stack

        for car in positions: 
            if not stack: 
                stack.append(car)

            if car_mappings[stack[-1]] < car_mappings[car]: 
                # this means that it is a new carfleet 
                stack.append(car)
        
        return len(stack )
            











