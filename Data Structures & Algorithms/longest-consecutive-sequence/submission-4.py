class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newlst = []
        output = []
        #cleans list for unique values
        for i in nums: 
            if i not in newlst:
                newlst.append(i)
        newlst = sorted(newlst)[::-1]
        if len(newlst) == 1:
            return 1
        for i in range(len(newlst[:-1])):
            current = newlst[i]
            next = newlst[i+1]

            if next+1 == current:
                output.append(current)
            if next+1 == current and newlst[-1] == next:
                output.append(next)
        return len(output)
        
        

