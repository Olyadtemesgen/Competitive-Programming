class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        length = 0
        
        heapq.heapify(matrix)
        
        while matrix and length < k - 1:
            
            val = heapq.heappop(matrix)
            val.pop(0)
            
            if val:
                heapq.heappush(matrix, val)
            
            length += 1
            
        return matrix[0][0]