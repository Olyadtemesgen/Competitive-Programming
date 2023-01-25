class Solution:
    def replaceElements(self, array: List[int]) -> List[int]:
                
        length = len(array)
        maximum = array[-1]
        
        for index in range(length - 2, -1, -1):

            array[index], maximum = max(array[index + 1], maximum), max(array[index], maximum)
        array[-1] = -1
        return array