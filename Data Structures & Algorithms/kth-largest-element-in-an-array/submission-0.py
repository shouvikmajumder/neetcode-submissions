import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            Problem notes:

            going to need some sort of maxHeap
            since its kth largest we can have a while loop where k>0 and heappop, when the loop breaks outs
            we just return the top element 
        
        '''

        # since there is no maxHeap we have to change the weights to negative

        minHeap = [-1 * num for num in nums]
        
        heapq.heapify(minHeap)
        
        print(minHeap)

        while k -1 > 0 :
            heapq.heappop(minHeap)
            k -= 1
        
        print(minHeap)
        
        return abs(minHeap[0])

