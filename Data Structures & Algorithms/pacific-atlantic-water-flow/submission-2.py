class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            Plan/Notes:     
                
                visited_set for both atlantic and pacific

                Dfs from Atlantic to Pacific and vice versa from Left to Right and Top to Bottom
        '''
        
        visited_from_pacific, visited_from_atlantic= set(), set() # [r,c]
        
        ROW , COL = len(heights), len(heights[0])

        def dfs(r,c,visited): 
            #we could just do this iteratively
            stack = [[r,c]]
            directions = [(1,0),(-1,0),(0,1), (0,-1)]

            while stack: 
                r,c = stack.pop()
                
                visited.add((r,c))

                for rd,cd in directions: 
                    nr,nc = r + rd, c + cd

                    if 0<= nr < ROW and 0 <= nc < COL and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited:
                        stack.append([nr,nc])

        for r in range(ROW): 
            dfs(r,0,visited_from_pacific) # Top --> Bottom
            dfs(r,COL - 1, visited_from_atlantic) #Bottom --> Top
        
        for c in range(COL): 
            dfs(0,c,visited_from_pacific) #left --> right
            dfs(ROW - 1, c, visited_from_atlantic) # right --> left

        common = []

        for r,c in visited_from_atlantic & visited_from_pacific: 
            common.append([r,c])
        
        return common