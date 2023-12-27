class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        dicts = defaultdict(int)
        
        walls = set(map(tuple, walls))

        grds = set(map(tuple, guards))
        for guard in guards:

            for i in range(guard[1] - 1, -1, -1):
                if  (guard[0], i) not in walls and (guard[0], i) not in grds and dicts[(guard[0], i)] != 1 and dicts[(guard[0], i)] != 3:
                    if (guard[0], i) in dicts:
                        dicts[(guard[0], i)] += 1
                    
                    else:
                        dicts[(guard[0], i)] = 1
                
                else:
                    break
            
            for i in range(guard[1] + 1, n):
                if  (guard[0], i) not in walls and (guard[0], i) not in grds and dicts[(guard[0], i)] != 1 and dicts[(guard[0], i)] != 3:
                    if (guard[0], i) in dicts:
                        dicts[(guard[0], i)] += 1
                    
                    else:
                        dicts[(guard[0], i)] = 1
                
                else:
                    break

            for i in range(guard[0] + 1, m):
                if (i, guard[1]) not in walls and (i, guard[1]) not in grds and dicts[(i, guard[1])] != 2 and dicts[(i, guard[1])] != 3:
                    if (i, guard[1]) in dicts:
                        dicts[(i, guard[1])] += 2
                    
                    else:
                        dicts[(i, guard[1])] = 2
                
                else:
                    break
            
            for i in range(guard[0] - 1, -1, -1):
                if (i, guard[1]) not in walls and (i, guard[1]) not in grds and dicts[(i, guard[1])] != 2 and dicts[(i, guard[1])] != 3:
                    if (i, guard[1]) in dicts:
                        dicts[(i, guard[1])] += 2
                    
                    else:
                        dicts[(i, guard[1])] = 2
                
                else:
                    break

        return n * m - len(dicts) - len(guards) - len(walls)