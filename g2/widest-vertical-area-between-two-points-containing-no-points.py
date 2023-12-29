class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        

        points.sort()
        answer = 0

        for index in range(len(points)):
            answer = max(answer, points[index][0] - points[index - 1][0])
        
        return answer