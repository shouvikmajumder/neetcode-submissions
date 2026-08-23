class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sums = {0:1}
        res = 0 
        curr_sum = 0

        for num in nums: 
            curr_sum += num
            diff = curr_sum - k
            # all we are going to do is try to see if diff is in the map 
            # if it is then we can add the frequency to res 
            
            # if the diff is not in the map, that also suggests that the current sum isnt either, so we must add it in 

            # however,if the diff is in the map, we add it to res
            res += prefix_sums.get(diff, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum,0) + 1 
        return res
