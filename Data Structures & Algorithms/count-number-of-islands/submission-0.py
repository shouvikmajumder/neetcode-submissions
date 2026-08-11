class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''
            Problem Approach: 
                The core idea here is to traverse throught the grid and everytime we
                encounter a "1", we call a dfs(r,c) which would traverse throught 
                the matrix and add all of the visited "1" into a visited set

                this visited set is then used to identify an island 

                we want to return the number of islands that we have found
        '''

        row, col = len(grid), len(grid[0])
        visited_set = set()


        def dfs(r,c): 
            if (r < 0 or c < 0 or r == row or c == col or grid[r][c] == "0" or (r,c) in visited_set): 
                return 
            
            visited_set.add((r,c))
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)

        num_of_islands = 0

        for r in range(row): 
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited_set: 
                    print(dfs(r,c))
                    num_of_islands += 1

        return num_of_islands        

