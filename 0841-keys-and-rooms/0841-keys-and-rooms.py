class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()

        def dfs(start):
            nonlocal visited

            if start in visited:
                return
            
            visited.add(start)

            for ss in rooms[start]:
                dfs(ss)
        
        dfs(0)

        return len(visited) == len(rooms)