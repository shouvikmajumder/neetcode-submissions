class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.kval = k

    def add(self, val: int) -> int:
        
        self.nums.append(val)

        outputlst = sorted(self.nums)[::-1]
        print(outputlst)

        return outputlst[self.kval-1]
