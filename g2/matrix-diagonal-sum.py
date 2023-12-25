class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        answer = 0
        for i in range(len(mat)):
            answer += mat[i][i] + mat[i][len(mat) - i - 1]
        
        if len(mat) % 2:
            answer -= mat[len(mat) // 2][len(mat) // 2]
        
        return answer
