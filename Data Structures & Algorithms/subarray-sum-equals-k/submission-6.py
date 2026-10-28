class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if sum(nums[i:j + 1]) == k and nums[i:j + 1] != [] :
                    res.append(nums[i:j + 1])
        
        print(res)

        return len(res)