class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3

        for num in nums: 
            count[num] += 1
        
        print(count)    
        
        index = 0
        for num_val in range(3):
            # this is because array only contains 0,1, or 2
            while count[num_val]: 
                nums[index] = num_val
                count[num_val] -= 1
                index +=1





