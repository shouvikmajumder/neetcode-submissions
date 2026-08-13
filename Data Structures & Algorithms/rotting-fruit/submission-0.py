from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            Problem Approach/Notes:
                We are going to interate throught the grid and if we find a rotten orange "2" we 
                want to add it in to a queue in order to perform bfs

                we also want a counter for the fresh fruit 

                if there are no fresh fruit at all we can just return time = 0 since all of the fruit is 
                already rotten

                in the queue we just want to increment the time per level and add the new row and col
                back into the queue 
        
                at the end we can return the total time

            Key Note: 
                during the while loop we and to keep going untill the queue is empty and untill we have to 
                fresh fruit left
        '''
        queue = deque([])
        rows , cols = len(grid), len(grid[0])
        fresh_fruit = 0
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: 
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1
        if fresh_fruit == 0:
            return time 

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while queue and fresh_fruit > 0: 
            # you want to check for any fresh_fruit and update it to rotten 
            for level in range(len(queue)): 
                r,c = queue.popleft()

                for row_direction, col_direction in directions: 
                    nr, nc = r + row_direction, c + col_direction

                    if 0<= nr <rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh_fruit -= 1
            time += 1 

        if fresh_fruit == 0:
            return time 

        return -1        

        


























        

















