class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #need to search for the correct range 
        # search within that range for the target


        left, right = 0, len(matrix) - 1

        
        while(left <= right):
            midp = (left + right) //2

            # now you need to check the range:
            
            small_blind, big_blind = matrix[midp][0],  matrix[midp][-1]

            if small_blind <= target <= big_blind: 
                # if its in range we can perfrom a binary search here
                search_matrix = matrix[midp] 
                left, right = 0, len(search_matrix) - 1

                while(left <= right):
                    midp_search_matrix = (left + right) // 2
                    if search_matrix[midp_search_matrix] == target: 
                        return True
                    elif search_matrix[midp_search_matrix] > target: 
                        right = midp_search_matrix - 1 

                    elif search_matrix[midp_search_matrix] < target: 
                        left = midp_search_matrix + 1
                return False
            elif target < small_blind: 
                right = midp - 1
                
            elif target > big_blind: 
                left = midp + 1

        return False
                



