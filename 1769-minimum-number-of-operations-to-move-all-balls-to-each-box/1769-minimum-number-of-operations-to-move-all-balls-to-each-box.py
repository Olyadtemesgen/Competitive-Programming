class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        first_index = []
        
        for index, char in enumerate(boxes):
            
            if int(char):
                first_index.append(index)
        
        answer = []
        
        for index, char in enumerate(boxes):
            result = 0
            
            for indexes in first_index:
            
                result += abs(indexes - index)
            
            answer.append(result)
        
        return answer