class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW,COL = len(matrix), len(matrix[0])
        top,bot = 0, ROW -1

        while(top<=bot):
            row = (top+bot)//2
            print(row)
            if target < matrix[row][0]:
                bot = row - 1
                print(bot)
            elif target > matrix[row][0]:
                top = row + 1
                print(top)
            else: 
                print("breaking")
                break 
        print(top,bot)
        
        row = matrix[(top+bot)//2]
        print(row)
        
        l,r = 0, len(row)-1

        while(l<=r):
            mp = (l+r)//2
            if target == row[mp]:
                return True
            elif target < row[mp]:
                r = mp - 1
            elif target > row[mp]:
                l = mp + 1 

        return False 
                


            