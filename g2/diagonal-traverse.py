class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        length_c = len(mat[0])
        length_r = len(mat)

        diagonal = length_c + length_r - 1
        
        answer = [[] for diagon in range(diagonal)]
        """This code goes through all 
        the values in the array and append
        it to the answer[row + col] or the answer"""
        for row in range(len(mat)):

            for col in range(len(mat[0])):
                
                answer[row + col].append(mat[row][col])
        real_answer = []
        print(answer)

        for i in range(diagonal):
            if i % 2:
                real_answer += answer[i]
                
            else:
                real_answer += list(reversed(answer[i]))
                
        return real_answer
