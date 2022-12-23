class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = float('inf')
        answer = 0
        #this iteration goes through all points and if it find valid it does what is requered
        for index, point in enumerate(points):
            
            if point[0] == x or point[1] == y:
                
                distance = abs(point[0] - x) + abs(point[1] - y)
                if  distance < result:
                    result = distance
                    answer = index
        #Return -1 if result does not changed
        return answer if result != float('inf') else -1
