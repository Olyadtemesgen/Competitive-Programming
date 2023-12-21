class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
                
        #row
        for row in board:
            counter = Counter(row)
            for x in counter:
                
                if x != '.' and counter[x] > 1:
                    return False
                
        #column
        for row in range(9):
            
            counter = {}
            for column in range(9):
                
                if board[column][row] in counter:

                    return False
                if board[column][row] != '.':
                    counter[board[column][row]]  = 1
            
        rows = [[],[],[],[],[],[],[],[],[]]
        
        for indx, row in enumerate(board):
            
            if indx < 3:
                for x in range(9):
                    if x < 3:
                        rows[0].append(row[x])
                    elif x < 6:    
                        rows[1].append(row[x])
                    else:
                        rows[2].append(row[x])
            elif indx < 6:
                for x in range(9):
                    if x < 3:
                        rows[3].append(row[x])
                    elif x < 6:
                        rows[4].append(row[x])
                    else:
                        rows[5].append(row[x])
            else:
                for x in range(9):
                    if x < 3:
                        rows[6].append(row[x])
                    elif x < 6:
                        rows[7].append(row[x])
                    else:
                        rows[8].append(row[x])
                
        for arr in rows:
            
            counter = Counter(arr)
            
            for count in counter:
                
                if count != '.' and counter[count] > 1:
                    return False
        return True