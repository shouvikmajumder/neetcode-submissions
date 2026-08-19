class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            if num not in map:
                map[num] = 1
            elif num in map:
                map[num] += 1 
        
        majority = max(map.values())

        for key in map: 
            if map[key] == majority: 
                return key
           

