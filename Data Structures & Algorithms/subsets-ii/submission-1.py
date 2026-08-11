class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
            Problem notes: 
                
                This is pretty much the same problem as Subsets1 the only thing you need to consder 
                is sorting the input array and checking for duplicates

        '''

        res = []
        def backtrack(index,sublst): 
            if index == len(nums):
                #out of range
                if sublst not in res: 
                    res.append(sublst.copy())
                return 
            
            sublst.append(nums[index])
            backtrack(index + 1, sublst)
            sublst.pop()
            backtrack(index + 1, sublst)

        nums.sort()
        backtrack(0,[])
        return res

