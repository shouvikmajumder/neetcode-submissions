from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_counter = Counter(nums)

        output = []

        for key in num_counter: 
            if num_counter[key] > (len(nums)/3):
                output.append(key)

        return output