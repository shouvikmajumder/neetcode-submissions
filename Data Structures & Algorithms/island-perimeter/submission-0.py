class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        ROW, COL  = len(grid), len(grid[0])

        def dfs(r,c):
            num_of_connected_components = 0

            stack = [(r,c)]
            directions = [(1,0),(-1,0),(0,-1),(0,1)]
            while stack: 
                r,c = stack.pop()
                num_of_connected_components += 1
                visited.add((r,c))
                for rd,cd in directions: 
                    nr,nc = r + rd, c + cd
                    if 0 <= nr< ROW and 0 <=nc < COL and grid[nr][nc] == 1 and (nr,nc) not in visited: 
                        stack.append((nr,nc))
            return num_of_connected_components

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    islands = dfs(r,c)
                    return (islands * 4) - ((islands -1 ) *2)
                     

