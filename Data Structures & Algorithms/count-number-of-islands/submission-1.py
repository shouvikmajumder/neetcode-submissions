class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            Plan: 
                iterate through the grid untill you see a 1
                porform a dfs on that cell and add it to a count of islands seen so far

        '''
        visited = set()
        numOfIslands = 0
        ROW, COL = len(grid), len(grid[0])
        
        def dfs(r,c): 
            stack = [(r,c)]
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            while stack: 
                r,c = stack.pop()

                visited.add((r,c))
            
                for rd,cd in directions: 
                    nr,nc = r + rd, c + cd         
                    if 0<= nr < ROW and 0 <= nc <COL and grid[nr][nc] == "1" and (nr,nc) not in visited: 
                        stack.append((nr,nc))


        for r in range(ROW): 
            for c in range(COL):
                print(grid[r][c])
                if grid[r][c] == "1" and (r,c) not in visited: 
                    dfs(r,c)
                    numOfIslands += 1
        return numOfIslands

