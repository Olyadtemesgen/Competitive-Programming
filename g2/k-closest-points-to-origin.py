class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        numbers = [[points[i][0]**2 + points[i][1] ** 2, i] for i in range(len(points))]
        numbers.sort()
        numbers = numbers[:k]
        
        answer = []

        for i in range(k):
            answer.append(points[numbers[i][1]])
        
        return answer