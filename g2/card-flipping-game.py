from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        df = dict()

        for index in range(len(fronts)):
            if fronts[index] == backs[index]:
                df[fronts[index]] = 0
            
            else:
                if fronts[index] not in df or df[fronts[index]]:
                    df[fronts[index]] = 1
                
                if backs[index] not in df or df[backs[index]]:
                    df[backs[index]] = 1
        
        answer = inf

        for dd in df:
            if df[dd]:

                answer = min(dd, answer)
        
        return answer if answer != inf else 0
