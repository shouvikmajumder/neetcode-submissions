class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            Approach for this problem seems to be building out a list, but to keep 
            track of 3 variables being current_index, sublist, and total 

            You can make a decision if the sum of the current sublst == total you can 
            return or if the index is out of range you can return as well

            Also make sure to put the copy of the sublist into the output array 
            so that you dont modify the decision tree itself
            
        '''
        res = []
        def dfs(index, sublst, total):
            
            #There are going to be 2 base cases 
            if total == target:
                res.append(sublst.copy())
                return 
            if index >= len(nums) or total > target:
                return #index would be out of bounds

            #here we can make the decision tree
            
            # This would include the current number
            sublst.append(nums[index])
            dfs(index, sublst, total + nums[index])
            
            #This would exclude the current number
            sublst.pop()
            dfs(index + 1, sublst, total)

        dfs(0,[],0)
        return res