from _heapq import heappop
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.minHeap = nums
        
        heapq.heapify(self.minHeap)
        # now your heap is initialized 
    
    def add(self, val: int) -> int:
        
        # idea here is you add the value and want to keep the k largert numbers in the heap
        heapq.heappush(self.minHeap,val)

        while len(self.minHeap) > self.k:
            smallest_element = self.minHeap
            heappop(self.minHeap)


        return self.minHeap[0]