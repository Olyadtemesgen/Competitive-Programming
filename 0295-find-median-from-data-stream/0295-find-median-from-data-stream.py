from sortedcontainers import SortedList

class MedianFinder:
    
    def __init__(self):
        
        self.heap = []
        heapq.heapify(self.heap)
        
        self.heap2 = []
        heapq.heapify(self.heap2)

    def addNum(self, num: int) -> None:

        
        if not self.heap and not self.heap2:
            self.heap2.append(num)
        
        elif self.heap2 and not self.heap:
            
            if self.heap2[0] >= num:
                heapq.heappush(self.heap, -num)
            
            else:
                heapq.heappush(self.heap, -heapq.heappop(self.heap2))
                heapq.heappush(self.heap2, num)
        
        else:
            
            if self.heap2[0] < num:
                heapq.heappush(self.heap2, num)
                
                if len(self.heap2) - 2 == len(self.heap):
                    heapq.heappush(self.heap, -heapq.heappop(self.heap2))
            
            else:
                
                heapq.heappush(self.heap, -num)
                
                if len(self.heap) - 2 == len(self.heap2):
                    heapq.heappush(self.heap2, -heapq.heappop(self.heap))
        # print(self.heap, self.heap2)
        
    def findMedian(self) -> float:
        
        if not self.heap:
            return self.heap2[0]
        
        if len(self.heap) == len(self.heap2):
            return (-self.heap[0] + self.heap2[0]) / 2
        
        elif len(self.heap) > len(self.heap2):
            return -self.heap[0]
        
        else:
            return self.heap2[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()