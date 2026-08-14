class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            Problem Approach: 
                What we could do is iterate throught all of the columns from top and bottom edges and call a dfs
                and add (r,c) values to a visited set if they are able to get to a path where they meet pacific and 
                atlantic regeions 

                WE do the exact same approach but with rows its left to right and right to left and also add 
                these values to a visited set
        '''

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r,c,visited): 
            # we are going to do iterative dfs
            directions = [(1,0),(-1,0), (0,1), (0,-1)]
            stack = [(r,c)]
            while stack: 
                r,c = stack.pop()
                visited.add((r,c))
                for rd, cd in directions: 
                    nr, nc = r + rd, c + cd 

                    if 0<=nr<rows and 0<=nc<cols and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited: 
                        stack.append((nr,nc))
                        
        #need to go from Top to bottom edeges and call a dfs on every cell 
        #also need to go from bottom to top
        for c in range(cols):
            # for the dfs input since we are only going for the top edge, row is going to be 0
            dfs(0,c,pacific)
            # from the bottom cell we are going to need row to be len(heights) -
            dfs(rows -1, c, atlantic) 
        # now we need to consider the side edges meaning left to right and right to left        
        for r in range(rows): 
            #left to right
            dfs(r, 0, pacific)
            #right to left
            dfs(r, cols -1, atlantic)

        # After every dfs traversal, you want to find the common coordinates between atlantic and pacific 
        # iterate throught both of these and add the unique values
        return [[r, c] for r, c in pacific & atlantic]





