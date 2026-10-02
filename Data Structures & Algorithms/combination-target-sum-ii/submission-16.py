class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(idx, sublst):
            
            if sum(sublst) == target and sublst not in res:
                res.append(sublst.copy())
                return  
            
            if idx == len(candidates):
                return

            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[idx]: 
                    continue
                else:
                    break
            
            sublst.append(candidates[idx])
            backtrack(idx + 1, sublst)
            sublst.pop()

            backtrack(idx + 1, sublst)

        backtrack(0,[])
        return res