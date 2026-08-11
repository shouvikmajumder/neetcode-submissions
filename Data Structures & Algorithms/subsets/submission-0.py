class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        stack = [(0,[])]


        res =[ ]

        while stack:

            index, subset = stack.pop()

            if index>= len(nums): 
                res.append(subset)
                continue
            
            #exclude 
            stack.append((index + 1, subset))
            #include
            stack.append((index + 1, subset + [nums[index]]))

        return res