class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        while k > len(nums): 
            k = (k // len(nums)) + 1 

        first_half = nums[:len(nums) - k]
        second_half = nums[len(nums) - k:]
        
        new_arr = second_half + first_half

        for index in range(len(new_arr)): 
            nums[index] = new_arr[index]
        
        