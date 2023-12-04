class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        current = 0
        index = 0
        answer = 0
        while index < len(plants):

            while index < len(plants) and current < capacity:
                current += plants[index]
                index += 1
                answer += 1
            
            print("index", index)
            print("answer", answer)
            
            if current > capacity:
                answer -= 1
                index -= 1

            if index < len(plants):
                answer += 2 * (index)

            current = 0
            print(answer)
        
        return answer