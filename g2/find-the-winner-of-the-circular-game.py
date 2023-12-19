class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        listt = list(range(1, n + 1))
        
        #By using circularly moving around the 
        deleted = k - 1
        index = 0
        
        while len(listt) - 1:
                
            while deleted:
                
                index += 1
                deleted -= 1
            
            deleted = k - 1
            index %= len(listt)
            
            listt.pop(index)
    
    
        return listt[0]