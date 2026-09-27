class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3 
        arr = []
        for num in nums: 
            count[num] += 1 
       
        for index,val in enumerate(count):
            arr += [index] * val
        
        for index in range(len(nums)):
            nums[index] = arr[index]
        