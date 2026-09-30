class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx,sublst):
            if idx == len(nums):
                res.append(sublst.copy())
                return 

            sublst.append(nums[idx])
            backtrack(idx + 1,sublst)

            sublst.pop()
            backtrack(idx + 1,sublst)

        backtrack(0,[])

        return res
        
