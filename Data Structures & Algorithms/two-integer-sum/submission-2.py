class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for index,value in enumerate(nums):
            diff = target - value
            if diff in check:
                return [check[diff],index]
            check[value] = index
        
