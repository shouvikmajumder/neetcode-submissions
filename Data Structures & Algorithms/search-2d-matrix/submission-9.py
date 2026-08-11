class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right = 0, len(matrix) - 1

        target_matrix = None

        while(left<=right):
            
            mid_point = (left+right)//2

            highest_val = matrix[mid_point][-1]
            lowest_val = matrix[mid_point][0]

            if target > highest_val: 
                left = mid_point + 1
                
            elif target < lowest_val:
                right = mid_point - 1
            
            elif target <= highest_val and target >= lowest_val: 
                target_matrix = matrix[mid_point]
                print(target_matrix)

                left, right = 0, len(target_matrix)

                while(left <= right): 
                    mid_point = (left + right)//2

                    if target_matrix[mid_point] == target: 
                        return True
                    elif target_matrix[mid_point] < target: 
                        left = mid_point + 1
                    elif target_matrix[mid_point] > target:
                        right = mid_point - 1
        return False



            





