class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        '''
            Problem notes:
                Apprach: The way to approachg this problem is by using backtracking 
                Every time we add an element to the result list we have 2 decisions we can possibly make
                    1) include the current elemetnt that the counter is on
                    2) exclucde the element entirely    

                We can recursively iterate throught the list untill the index is bigger than len(nums)                
        '''

        res = []
        sublst = [] 

        def dfs(index): 

            if index > len(nums) - 1:
                res.append(sublst.copy())
                return res  
        
            #1 decision where you include the element in the sublist
            sublst.append(nums[index])
            dfs(index + 1)

            #2 decisiotn wher you dont include the element in the sublist 
            sublst.pop()
            dfs(index + 1)


        dfs(0)
        return res

