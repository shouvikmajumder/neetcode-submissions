class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ''' 
            Problem Approach: 
                I think I am going to take some inspo from the permutations problem

                We are essentially going to do a recursive call on subsetsWithDup where we chunk the list by
                passing in nums[1:]

                we will also have a res list initialized that is going to contain the sublists 

                since we did not include the nump[1:] we will and len(nums[1:]) + 1 iterations where we can append 
                a copy of the sublist where we choose to either include or exclude the current num
 
                return res
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

