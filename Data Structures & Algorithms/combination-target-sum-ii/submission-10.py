class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''Container, 
            Problem Notes: 

                We can include a similar implementation to combinationSum1, the key differnce here 
                is that we can inlude a value once instead of multiple times
        
                Approach: 
                    We are going to build out a decision tree via dfs, and this can be done recursively

                    Stop conditionsn are goign to be when index is either out of range or our total sum 
                    is greater that the target
                    
                    Also a key note, when appending a sublst to the res, we have to append the copy
                    so that it doesnt affect the decision tree

                Post Solve Attempt:

                    Better to build the tree iterativly, through using stack as recursion seems to be pretty expensive memory 
                    and slow speed wise
        ''' 
        stack = [[0,[],0]]
        res = []
        duplicates = []
    
        while stack: 

            index, curr_sublst, total = stack.pop()

            if total == target:
                #this means that we have a valid combination
                if sorted(curr_sublst) not in duplicates:
                    duplicates.append(sorted(curr_sublst))
                    res.append(curr_sublst.copy())
                                
            if total > target or index > len(candidates) - 1:
                continue 
            
            # Here you have to include or exlude into the sublst        
            stack.append([index + 1, curr_sublst + [candidates[index]], total + candidates[index]])
            #exclusion
     
            stack.append([index + 1, curr_sublst, total]) 
        
        return res
                




        


