class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROW, COL = len(board), len(board[0])

        for row_idx in range(ROW):
            seen = set()
            for col_idx in range(COL):
                item = board[row_idx][col_idx]
                
                if item == ".":
                    continue
                elif item in seen: 
                    return False 
                else: 
                    seen.add(item)

        for col_idx in range(COL):
            seen = set()
            for row_idx in range(ROW):
                item = board[row_idx][col_idx]                
                if item == ".":
                    continue
                elif item in seen: 
                    return False 
                else: 
                    seen.add(item)
        #now we need to evaluate each individaul square
        for square in range(len(board)):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    item = board[row][col]                
                    if item == ".":
                        continue
                    elif item in seen: 
                        return False 
                    else: 
                        seen.add(item)
        return True

