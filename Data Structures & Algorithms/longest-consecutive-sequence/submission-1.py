class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nums = nums[::-1]
        outputcount = []
        print(nums)
        for index in range(len(nums[:-1])):
            next = nums[index + 1]
            current = nums[index]
            if (current-1 == next):
                outputcount.append(current)
        return len(outputcount)+1
        


