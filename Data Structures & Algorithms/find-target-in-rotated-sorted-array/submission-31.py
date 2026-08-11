class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        '''
            [4,5,6,7,8,9] rotated 3 times --? [7,8,9,4,5,6] target = 5
            l,r,mp = 7,6,4

            we could start off by looking throught the sorted region 
                - can do this by checking if midp > left #left side is sorted 
                - if mid < right means that the right region is sorted        

                - if the target is not in one of the regions you can take eitehr the left 
                or the right pointer and move it accordingly 

        '''
        left, right = 0, len(nums) - 1

        while left <= right: 
            mp = (left + right) // 2 

            if nums[mp] == target:
                return mp

            elif nums[mp] < nums[right]: 
                if nums[mp] < target <= nums[right]: 
                    left = mp + 1
                else: 
                    #check the other region for the target
                    right = mp - 1
            else: 

                #left region is sorted
                if nums[left] <= target < nums[mp]: 
                   right = mp - 1
                else: 
                    left = mp + 1


        return -1
        