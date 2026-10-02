class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(idx, sublst):
            
            if sum(sublst) == target:
                res.append(sublst.copy())
                return  
            
            if idx == len(candidates):
                return

            sublst.append(candidates[idx])
            backtrack(idx + 1, sublst)
            sublst.pop()

            backtrack(idx + 1, sublst)

        backtrack(0,[])

        unque_subsets = []

        for sublst in res: 
            if sublst not in unque_subsets: 
                unque_subsets.append(sublst)

        return unque_subsets





