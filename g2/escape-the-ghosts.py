class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        distance = inf

        for ghost in ghosts:
            distance = min(distance, abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]))
            
        return abs(target[0]) + abs(target[1]) < distance

