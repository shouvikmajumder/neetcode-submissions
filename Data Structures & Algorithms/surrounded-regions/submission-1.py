from collections import deque  
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        Problem Approach/Notes:

            Since one of the primary ways to categorize if something isnt a region is if its connected to the 
            borders. One thing we cna do is perform a dfs of every border coordinate that is "O" and  

            For the bfs if we do find any other zeros we can replace the O with a T being a temporary value

            after wards the remaining zeros we can replace with an X since we determined that it is a valid 
            region as long as it didnt get picked up by the dfs           
        '''

        row, col = len(board), len(board[0])

        def bfs(r,c):
            queue = deque([(r,c)])

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            while queue: 
                r,c = queue.popleft()
                board[r][c] = "T"

                for rd, cd in directions: 
                    nr,nc = r +rd , c + cd 

                    # we want to make sure that nr and nc are in range and coordingte to 0 
                    if  0 <= nr < row and 0 <= nc < col and board[nr][nc] == "O": 
                        queue.append((nr,nc))

        for r in range(row):
            for c in range(col): 
                if ((r in (0, row-1) or c in (0, col -1)) and board[r][c] == "O"):
                    bfs(r,c)


        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T": 
                    board[r][c] = "O"
            