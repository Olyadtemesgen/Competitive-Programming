class Solution:
    def interchangeableRectangles(self, rectangle: List[List[int]]) -> int:
        
        for x in range(len(rectangle)):
            
            rectangle[x] = rectangle[x][1]/ rectangle[x][0]
        
        rectangle.sort()
        
        left = 0
        right = 0
        result = 0
        
        while right < len(rectangle):
            
            while right < len(rectangle) and rectangle[left] == rectangle[right]:
                right += 1
            
            aa = (right - left - 1)
            result += int((aa ** 2 + aa) / 2)
            
            left = right
        
        return result