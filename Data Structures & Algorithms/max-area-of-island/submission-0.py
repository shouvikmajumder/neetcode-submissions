class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            Problem Approach:
                
                We are going to loop throught the grid untill we find a "1" being an island
                    - We can run a dfs and counter up all of the 1's neighboring, which would 
                    give us the area    

                    - In the orignal looping we would have check that would compare the current
                    area witht the greatest area we have seen so far 
                    
                    - At the end we can return max_area_island 
        '''
        rows, cols = len(grid), len(grid[0])    
        visited_set = set()

        def dfs(r,c): 
            if(r<0 or c<0 or r == rows or c == cols or grid[r][c] == 0 or (r,c) in visited_set): 
                return 0
            visited_set.add((r,c))
            return 1 + (dfs(r+1,c) + dfs(r - 1,c) + dfs(r,c + 1) + dfs(r,c -1))

        max_area_island = 0

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1 and (r,c) not in visited_set: 
                    curr_area = dfs(r,c)
                    print(curr_area)
                    max_area_island = max(max_area_island,curr_area)

        return max_area_island