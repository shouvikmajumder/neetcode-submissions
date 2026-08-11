class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left_ptr, right_ptr = 0, len(matrix) - 1 

        target_matrix = []

        while(left_ptr <= right_ptr):

            midpoint_ptr = (left_ptr + right_ptr)//2

            low = matrix[midpoint_ptr][0]
            high = matrix[midpoint_ptr][-1]

            if target > high: 
                left_ptr += 1
            elif target < low: 
                right_ptr -= 1 
            elif target >= low and target <= high:
                target_matrix = matrix[midpoint_ptr]
                left_ptr +=1 
                right_ptr -=1 


        print(target_matrix)

        left_ptr, right_ptr = 0, len(target_matrix) -1

        while(left_ptr < right_ptr):
            
            midp = (left_ptr + right_ptr) // 2 
            # print(left_ptr,right_ptr)

            if target_matrix[midp] == target:
                return True
            elif target_matrix[midp] > target: 
                right_ptr -= 1 
            elif target_matrix[midp] < target: 
                left_ptr += 1         
        
        return False
            
