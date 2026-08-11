class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        '''
            Problem Notes: 

                We can include a similar implementation to combinationSum1, the key differnce here 
                is that we can inlude a value once instead of multiple times
        
                Approach: 
                    We are going to build out a decision tree via dfs, and this can be done recursively

                    Stop conditionsn are goign to be when index is either out of range or our total sum 
                    is greater that the target
                    
                    Also a key note, when appending a sublst to the res, we have to append the copy
                    so that it doesnt affect the decision tree
        ''' 
        res = []
        sublst = [] 
        
        candidates.sort()
        print(candidates)        
        def dfs(index, curr, total): 
            if total == target: 
                if curr not in res: 
                    res.append(curr.copy())            
                return
            if index > len(candidates) - 1 or total > target: 
                return
     
            # Now we have to determine the inclusion and exclusion criteria
            # since you can only add each element once, you will have progress the index every itr 
            
            curr.append(candidates[index]) #including the cadidate
            dfs(index + 1, curr, total + candidates[index]) 

            curr.pop()
            dfs(index + 1, curr, total) #excluding the candidate

        dfs(0, [], 0)
        return res











