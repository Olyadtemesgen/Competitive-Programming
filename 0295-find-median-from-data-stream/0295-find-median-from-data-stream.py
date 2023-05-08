from sortedcontainers import SortedList
class MedianFinder:
    
    def __init__(self):
        
        self.heap = SortedList()

    def addNum(self, num: int) -> None:
        # if not self.heap:
        self.heap.add(num)
        # print(self.heap)
        
    def findMedian(self) -> float:
        
        if len(self.heap) % 2:
            return self.heap[len(self.heap) // 2]
        
        else:
            length = len(self.heap) // 2
            
            val1 = self.heap[length]
            val2 = self.heap[length - 1]
            
            return (val1 + val2) / 2
            

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()