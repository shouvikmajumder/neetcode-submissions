class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL  = len(grid), len(grid[0])

        def dfs(r,c):
            perimeter = 0
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            # we want to add the perimeter if we go out of bounds
            visited = {(r,c)}
            stack = [(r,c)]
            while stack:
                r,c = stack.pop()
              

                for rd,cd in directions: 
                    nr,nc = r + rd, c + cd

                    if nr >= ROW or nr < 0 or nc >= COL or nc < 0 or grid[nr][nc] == 0:
                        perimeter +=1 
                    elif (nr,nc) not in visited:
                        stack.append((nr,nc))
                        visited.add((nr,nc))

            return perimeter
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return dfs(r,c)
                     

