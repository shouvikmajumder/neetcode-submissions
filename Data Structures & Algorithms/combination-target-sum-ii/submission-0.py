class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #Approach: DFS throught the candidtes, 
        # going to have a stack with (index, [], total)
        # Decieve exlusion and inclusion criteria:

        stack = [(0,[],0)]  

        res = []

        while stack:
            index, subarray, total = stack.pop()

            if total == target: 
                if subarray not in res:
                    res.append(subarray)
                continue

            if index>= len(candidates) or total > target:
                continue
            
            stack.append((index + 1, subarray, total ))
            stack.append((index + 1, subarray + [candidates[index]], total + candidates[index]))
            
        return res
