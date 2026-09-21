import statistics 
class MedianFinder:

    def __init__(self):
        self.numlst = []

    def addNum(self, num: int) -> None:
        self.numlst.append(num)

    def findMedian(self) -> float:
        return statistics.median(self.numlst)

        