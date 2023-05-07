class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        difference = []
        
        for vals in range(1, len(heights)):
            
            difference.append(heights[vals] - heights[vals - 1])
            
        # print(difference)
        index = 0
        
        heap = []
        
        heapq.heapify(heap)
        
        while ladders and index < len(difference):
            
            if difference[index] > 0:
                
                ladders -= 1
                
                heapq.heappush(heap, difference[index])
            
            index += 1
        
        if index == difference:
            return len(heights)
        # print(bricks, index, difference)
        
        while bricks >= 0 and index < len(difference):
            
            if difference[index] > 0:
                
                heapq.heappush(heap, difference[index])
                
                val = heapq.heappop(heap)
                
                bricks -= val
                
            if bricks >= 0:
                index += 1
        
        if index == len(difference):
            return len(heights) - 1
        
        else:
            return index