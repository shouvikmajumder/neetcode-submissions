class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        visited = {}

        for index in range(len(nums)): 
            num = nums[index]

            if num not in visited:
                visited[num] = index
            elif num in visited:
                if abs(visited[num] - index) <= k:
                    return True

        return False