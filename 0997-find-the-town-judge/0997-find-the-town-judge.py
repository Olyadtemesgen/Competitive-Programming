class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        saved = set()
        if not trust:
            if n == 1:
                return 1
            return -1

        for x in range(len(trust)):
            
            saved.add(trust[x][0])

        if len(saved) == n:
            return -1
        
        else:
            for x in range(1, n + 1):
                if x not in saved:break
            
            aa = set()

            for xy in range(len(trust)):
                if trust[xy][1] == x:
                    aa.add(trust[xy][0])
                
            if len(aa) == n - 1:
                return x
            
            return -1
