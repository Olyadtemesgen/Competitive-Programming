class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        answer = 0

        for index in range(len(points) - 1):

            one = points[index + 1][0] - points[index][0]
            two = points[index + 1][1] - points[index][1]

            abs1, abs2 = abs(one), abs(two)

            if abs1 > abs2:
                answer += abs2

                answer += abs(points[index + 1][0] - points[index][0] - (-1 + 2 * (one * two >= 0)) * two)
                

            
            elif abs1 < abs2:
                answer += abs1
                answer += abs(points[index + 1][1] - points[index][1] - (-1 + 2 * (one * two >= 0)) *one)
            
            else:
                answer += abs1
        
        return answer