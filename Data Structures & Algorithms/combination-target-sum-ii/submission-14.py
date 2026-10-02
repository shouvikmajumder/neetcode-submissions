class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(idx, sublst):
            
            if sum(sublst) == target and sublst not in res:
                res.append(sublst.copy())
                return  
            
            if idx == len(candidates):
                return
            
            sublst.append(candidates[idx])
            backtrack(idx + 1, sublst)
            sublst.pop()

            backtrack(idx + 1, sublst)
            
            
        backtrack(0,[])
        return res