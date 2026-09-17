class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k 
        self.queue = []

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        else:
            self.queue.append(value)
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else: 
            #we want to pop from the beginning of the queue 
            self.queue = self.queue[1:]
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1 
        return self.queue[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1 
        return self.queue[-1]

    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        return False
        

    def isFull(self) -> bool:
        if len(self.queue) >= self.size:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()