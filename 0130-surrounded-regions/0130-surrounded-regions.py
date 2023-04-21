class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        result = []
        res = set()
        res2 = set()
        vv = set()
        flag = True
        
        def dfs(row, col, visited):
            
            nonlocal res
            nonlocal vv
            nonlocal flag
            value = row * len(board[0]) + col
            if  value in visited or row < 0 or col < 0 or col >= len(board[0]) or row >= len(board) or board[row][col] != "O":
                
                return
            
            if row == 0 or col == 0 or  col == len(board[0]) - 1 or row == len(board) - 1:
                flag = False
                
            visited.add(value)
            vv.add(value)
            res.add(value)
            
            dfs(row + 1, col , visited)
            dfs(row - 1, col , visited)
            dfs(row, col + 1 , visited)
            dfs(row, col - 1 , visited)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                value = row * len(board[0]) + col
                flag = True
                vv = set()
                if board[row][col] == "O" and value not in res:
                    print(res)
                    dfs(row, col, set())
                    if flag:
                        res2 = res2.union(vv)
        
        for re in res2:
            row = re // len(board[0])
            col = re % len(board[0])
            
            board[row][col] = 'X'
        
        return board