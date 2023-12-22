class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        
        # half = len(image) // 2

        for row in range(len(image)):
            
            right = len(image) - 1
            left = 0
            while right >= left:
                image[row][left], image[row][right] =1- image[row][right],  1 - image[row][left]
                right -= 1
                left += 1
        
        return image