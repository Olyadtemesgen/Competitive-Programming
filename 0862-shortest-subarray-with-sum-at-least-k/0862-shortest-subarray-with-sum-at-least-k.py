class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        for x in nums:
            if x >= k:return 1
        prefix = [0]
        answer = float('inf')
        
        for x in range(len(nums)):
            
            prefix.append(prefix[x] + nums[x])
            # lens = x
            # while lens > -1 and x - lens + 1 < answer:
            #     if prefix[-1] - prefix[lens] >= k:
            #         answer = min(x - lens + 1, answer)
            #         break
            #     lens -= 1
        
        queue = collections.deque()
        
        for index, value in enumerate(prefix):
            
            while queue and value - prefix[queue[0]] >= k:answer = min(answer, index - queue.popleft())
            
            while queue and value <= prefix[queue[-1]]:
                queue.pop()
            
            queue.append(index)
        
        return answer if answer != float('inf') else -1