class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        lr_diagonals = [king]
        rl_diagonals = [king]
        x_positions = [king]
        y_positions = [king]

        for  q_position in queens:
            
            if  (q_position[0] - king[0] == q_position[1] - king[1]):
                lr_diagonals.append(q_position)

            elif (q_position[0] - king[0] == -1 * (q_position[1] - king[1])):
                rl_diagonals.append(q_position)
            
            elif q_position[0] == king[0]:
                x_positions.append(q_position)
            
            elif q_position[1] == king[1]:
                y_positions.append(q_position)
        
        rl_diagonals.sort(key=lambda x: x[1])
        lr_diagonals.sort()
        x_positions.sort()
        y_positions.sort()
        
        

        result = []
        k_position = x_positions.index(king)
        if len(x_positions) > 1:
            if k_position == len(x_positions) - 1:
                result.append(x_positions[k_position - 1])
            
            elif k_position == 0:
                result.append(x_positions[k_position + 1])
            
            else:
                result.append(x_positions[k_position - 1])
                result.append(x_positions[k_position + 1])

        k_position = y_positions.index(king)
        if len(y_positions) > 1:
            if k_position == len(y_positions) - 1 and k_position != 0:
                result.append(y_positions[k_position - 1])
            
            elif k_position == 0 and len(y_positions) > 1:
                result.append(y_positions[k_position + 1])
            
            else:
                result.append(y_positions[k_position - 1])
                result.append(y_positions[k_position + 1])
        
        k_position = lr_diagonals.index(king)
        if len(lr_diagonals) > 1:
            if k_position == len(lr_diagonals) - 1:
                result.append(lr_diagonals[k_position - 1])
            
            elif k_position == 0:
                result.append(lr_diagonals[k_position + 1])
            
            else:
                result.append(lr_diagonals[k_position - 1])
                result.append(lr_diagonals[k_position + 1])

        k_position = rl_diagonals.index(king)
        if len(rl_diagonals) > 1:
            if k_position == len(rl_diagonals) - 1: 
                result.append(rl_diagonals[k_position - 1])
            
            elif k_position == 0:
                result.append(rl_diagonals[k_position + 1])
            
            else:
                result.append(rl_diagonals[k_position - 1])
                result.append(rl_diagonals[k_position + 1])   

        for x in range(len(result)):
            if result[x] in result[:x]:
                result.pop(x)

        return result
