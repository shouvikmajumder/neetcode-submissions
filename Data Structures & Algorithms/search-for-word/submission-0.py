class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
            Problem Approach: 
                You want to do a dfs on the rows and columns

                The inclusion and exclusion criteria is basically 
                deciding if you want to add the path to the set or
                not

        '''

        ROWS, COLS = len(board)-1, len(board[0])-1 
        pairs = set()

        print(ROWS,COLS)

        def dfs(r,c,index):
            if index == len(word) - 1:
                return True 
            
            if (r > ROWS or c>COLS or board[r][c] != word or (r,c) in pairs):
                return False
            
            pairs.add((r,c))
            res = (
                dfs(r + 1,c,index + 1) or
                dfs(r - 1,c,index + 1) or 
                dfs(r,c + 1,index + 1) or
                dfs(r,c - 1,index + 1) 
            )
            pairs.remove((r,c))

            return res    

        for r in range(ROWS): 
            for c in range(COLS): 
                if dfs(r,c,0):
                    return True
        return False

    