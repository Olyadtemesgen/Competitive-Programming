class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        one = edges[0]
        two = edges[1]
        
        for x in one:
            
            for y in two:
                
                if x == y:
                    return x
        