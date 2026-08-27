class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        write_pointer = 0

        for read_pointer in range(len(nums)):       
            # we ant read pointer to find any no zeros and swap it with write pointer which is going to point to a zero

            if nums[read_pointer] != 0: 
                # we can do a swap
                nums[write_pointer],nums[read_pointer] = nums[read_pointer], nums[write_pointer]
                write_pointer += 1
                