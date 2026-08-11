class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
            Problem Approach: 
                We can solve this problem through the iteration method
                    - we can recursively splice the input array 
                    - once we do that we can iterate throught the permutations that we have
                    - since we spliced it we can traverse the array len(p) + 1 times 
                    - You can then insert the first integer(nums[0]) into the sublst using insert and append it to the result
        '''

        if len(nums) == 0: 
            return [[]]
        
        res = [ ]
        permutations = self.permute(nums[1:])   

        for p in permutations: 
            for index in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(index,nums[0])
                res.append(p_copy)
        return res