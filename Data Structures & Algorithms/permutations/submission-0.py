class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
         
        if len(nums) == 0:
            return [[]]
        
        permutations = self.permute(nums[1:])
        res = []

        for p in permutations: 
            for index in range(len(p) + 1):
                # I think you can insert at the end of this list, by using 1 + more than the current index at the end of list
                p_copy = p.copy() # copying the permution and inserting 1 in different parts
                p_copy.insert(index,nums[0])

                res.append(p_copy)
        return res
                