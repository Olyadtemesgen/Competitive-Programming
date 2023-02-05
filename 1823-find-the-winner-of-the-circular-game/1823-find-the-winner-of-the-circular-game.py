class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        the_numbers = list(range(n, 0, -1))
        
        length = k - 1
        
        while len(the_numbers) - 1:
            
            while length:
                
                the_numbers.insert(0, the_numbers.pop())
                
                length -= 1
            
            length = k - 1
            
            the_numbers.pop()
        return the_numbers[0]