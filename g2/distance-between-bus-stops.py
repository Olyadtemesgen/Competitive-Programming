class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        total = sum(distance)

        starts = min(start, destination)
        end = max(start, destination)

        answer = 0

        for index in range(starts, end):
            answer += distance[index]
        
        print(answer)
        return min(total - answer, answer)
