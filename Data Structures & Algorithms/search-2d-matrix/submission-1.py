class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        
        l,r = 0, len(matrix) - 1
        
        while(l<=r):
            mp = (l+r)//2
            
            if matrix[mp][0]<=target<=matrix[mp][-1]:
                left,right = 0, len(matrix[mp]) - 1
                while(left<=right):
                    midp = (left + right)//2 
                    if matrix[mp][midp] == target:
                        return True
                    elif matrix[mp][midp] > target:
                        right = midp - 1
                    elif matrix[mp][midp] < target:
                        left = midp + 1
                return False
                
            elif target < matrix[mp][0]:
                r = mp - 1
            else:
                l = mp + 1
                
        return False