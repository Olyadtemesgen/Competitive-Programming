class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        
        tasks.sort(reverse=True)

        processorTime.sort()


        left = 0
        answer = 0

        for number in processorTime:
            answer = max(answer,  number + tasks[left])
            left += 4
        
        return answer