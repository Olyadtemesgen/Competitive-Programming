class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        go_before = set()
        def findeach(row, col, index):
            
            if index == len(word):
                return True
            
            
            if row < 0 or col < 0 or row > len(board)  - 1 or col > len(board[0]) - 1  or board[row][col] != word[index] or ((row, col) in go_before):
                return False
            
            go_before.add((row, col))
            
            answer =  findeach(row + 1, col , index + 1) or findeach(row - 1, col, index + 1) or findeach(row, col + 1, index + 1) or findeach(row, col - 1, index + 1)
            go_before.remove((row, col)
                            )
            return answer
        for x in range(len(board)):
            for y in range(len(board[0])):
                if findeach(x, y, 0):
                    return True
        
        return False