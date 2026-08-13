from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            Problem Approach/Notes:
                This problem a dfs would be too inefficien. I tried it and got the max recursion depth error
                
                Bfs is the right approach here 

                Core Algo:
                    Iterate through the grid and find the coordinates with the zeros and append it to a queue
                    
                    Go throught the queue and see apply the directions left right up and down to the r and c 
                    and determine if you find an island, if you do you can update grid[r][c] = grid[nr][nc] + 1
                    where you can push [nr,nc] back into the queue
        '''
        queue = deque([])
        rows,cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r,c])

        #queue is going to contain all coordinate pairs for all of the treasure chests
        directions = [(1,0),(-1,0),(0,1),(0,-1)] #these are the different directions for bfs to work

        while queue:
            r,c = queue.popleft()
        
            #we want to find islands
            for rd,cd in directions:
                nr, nc = r + rd , c + cd

                #need to check if it is in range
                
                if nr>=0 and nr < rows and nc >=0 and nc < cols and grid[nr][nc] == 2147483647: 
                    #this means that we have found an island 
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append([nr,nc])




