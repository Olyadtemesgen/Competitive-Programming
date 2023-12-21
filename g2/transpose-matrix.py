class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l2=[]
        for j in range(0,len(matrix[0])):
            l1=[]
            
            for i in matrix:
                l1.append(i[j])
            
            l2.append(l1)
   
        return l2