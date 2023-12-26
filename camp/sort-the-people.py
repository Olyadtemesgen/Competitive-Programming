class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        #by using bubble sort reversed
#         for x in range(len(names)):
            
#             for y in range(len(names) - x - 1):
                
#                 if heights[y] < heights[y + 1]:
                    
#                     heights[y], heights[y + 1] = heights[y + 1], heights[ y]
                    
#                     names[y], names[y + 1] = names[y + 1], names[y]
        
#         return names
        #by using selection sort
        for x in range(len(names)):
            minimum = heights[x]
            index = x
            for y in range(x + 1, len(names)):
                xx = minimum 
                minimum = min(minimum, heights[y])
                if xx != minimum:
                    index = y
            
            names[index], names[x] = names[x], names[index]
            heights[index], heights[x] = heights[x], heights[index]
        names.reverse()
        return names
                