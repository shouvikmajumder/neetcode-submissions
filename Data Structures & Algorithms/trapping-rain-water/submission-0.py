class Solution:
    def trap(self, height: List[int]) -> int:
        # need to make an array that gets the max on the left side

        # make another array that gets max of the left side array

        # third array that gets the min of each of th prev array indexs 

        # count that counts the min() - current index of heigh array

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(len(height)):

            if i != 0:
                left_max[i] = max(height[:i])
        
        for i in range(len(height)):
            
            if i != len(height) -1:
                right_max[i] = max(height[i + 1:])
        
        comp_arr = []
        output_arr = []

        for i in range(len(height)):
            comp_arr.append(min(left_max[i], right_max[i]))

        for i in range(len(height)):
            output_arr.append(comp_arr[i]- height[i])

        water_area_total = 0

        for i in output_arr:
            if i > 0: 
                water_area_total += i
        return water_area_total
        
        