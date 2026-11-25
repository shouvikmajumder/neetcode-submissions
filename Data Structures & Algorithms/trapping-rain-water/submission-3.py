class Solution:
    def trap(self, height: List[int]) -> int:   
        #max height on the left side 
        #max height on the right side
        #write a comparision array that takes the min of left and right per index
        
        left_side_arr = [0] * len(height)
        right_side_arr = [0] * len(height)

        #left side max 
        local_max_left_side = 0

        for idx in range(len(left_side_arr)):
            curr = height[idx]
            
            if local_max_left_side > curr: 
                left_side_arr[idx] = local_max_left_side

            local_max_left_side = max(local_max_left_side,curr)
        
        local_max_right_side = 0

        for idx in range(len(right_side_arr) - 1, -1, -1):
            curr = height[idx]

            if local_max_right_side > curr: 
                right_side_arr[idx] = local_max_right_side
            local_max_right_side = max(local_max_right_side, curr)
        

        trapped_boundaries = []

        for idx in range(len(height)):
            trapped_boundaries.append(min(left_side_arr[idx],right_side_arr[idx]))

        counter = 0 

        for idx in range(len(trapped_boundaries)): 

            if trapped_boundaries[idx] >= height[idx]:
                counter += trapped_boundaries[idx] - height[idx]

        return counter


