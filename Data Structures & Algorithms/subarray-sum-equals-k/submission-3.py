class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force, O(n^2) sol where we are just oging to interate over the nums untill we get to k

        res = 0

        for i in range(len(nums)): 
            for j in range(i,len(nums)):
                subsum = sum(nums[i: j + 1])
                if subsum == k:
                    res += 1
        return res 
