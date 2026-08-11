class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        outputcount = []
        for index in range(1,len(nums[:-1])):
            currvalue = nums[index-1]
            nextvalue = nums[index]
            
            if outputcount == []:
                outputcount.append(currvalue)
            if ((currvalue+1) == nextvalue) or ((currvalue) == nextvalue):
                outputcount.append(currvalue)
        if outputcount[0] == 0:
            return len(outputcount)
        return len (outputcount)-1

