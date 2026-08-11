class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1

        while(left<right):
            if nums[left] == target:
                return left
            if nums[left]< nums[(left+right)//2]:
                left = ((left+right)//2)+1
        return -1 