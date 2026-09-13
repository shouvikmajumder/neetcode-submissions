import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        '''
            hashmap where difference in key and element is the value {diff : [nums]}
        '''

        mappings = {}

        for num in arr:
            absol_diff = abs(num - x)

            if absol_diff not in mappings: 
                mappings[absol_diff] = [num]
            else: 
                mappings[absol_diff].append(num)
        diffs = list(mappings)
        diffs.sort()        
        print(diffs)

        outputarr = []

        for key in diffs: 
            for val in mappings[key]: 
                if len(outputarr) == k:
                    return sorted(outputarr)
                else: 
                    outputarr.append(val)

        return outputarr

            