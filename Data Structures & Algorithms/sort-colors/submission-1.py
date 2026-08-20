class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0,0,0]

        for num in nums: 
            #0,1,2
            if num == 0: 
                count[0] += 1
            elif num == 1:
                count[1] += 1
            elif num == 2: 
                count[2] += 1 

        index = 0
        count_index = 0
        for val in range(3): # 0, 1 , and 2 
            while count[count_index]: 
                nums[index] = val
                count[count_index] -= 1
                index += 1
            count_index += 1

            
