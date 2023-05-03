class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        answer = [[0 for x in range(len(mat[0]))] for y in range(len(mat)) ]
        
        length = 0
        
        queue = deque()
        visited = set()
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                
                if not mat[row][col]:
                    queue.append((row, col))
        
                    visited.add((row, col))
        # print(queue)
        
        while queue:

            lengs = len(queue)

            for lens in range(lengs):

                row, col = queue.popleft()
                # visited.add((row, col))
                
                if mat[row][col]:
                    answer[row][col] = length


                if row < len(mat) - 1 and (row + 1, col) not in visited:
                    queue.append((row + 1, col))
                    visited.add((row + 1, col))
        
                if row and (row - 1, col) not in visited:
                    queue.append((row - 1, col))
                    visited.add((row - 1, col))

                if col < len(mat[0]) - 1 and (row, col + 1) not in visited:
                    queue.append((row, col + 1))
                    visited.add((row, col + 1))

                if col and (row, col - 1) not in visited:
                    queue.append((row, col - 1))
                    visited.add((row, col - 1))

            length += 1

        return answer
        