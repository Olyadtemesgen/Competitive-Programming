class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        tickets = deque(tickets)

        indexs = k
        
        length = len(tickets)
        index = 0
        answer = 0
        while tickets[indexs]:
            
            tickets[0] -= 1
            if tickets[0]:
                tickets.append(tickets.popleft())
    
            else:
                if not tickets[indexs]:
                    break
                tickets.popleft()
    
            indexs = (indexs - 1) % len(tickets)

            answer += 1
            
                
        return answer + 1