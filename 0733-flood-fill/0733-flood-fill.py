class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc]==color:
            return image
        saved = image[sr][sc]
        def dfs(sr,sc):
            nonlocal saved
            
            if sr>=len(image) or sr<0 or sc>= len(image[0]) or sc<0:
                return

            if image[sr][sc]!=saved:
                return
            
            image[sr][sc]=color
            
            dfs(sr-1,sc) 
            dfs(sr+1,sc) 
            dfs(sr,sc-1) 
            dfs(sr,sc+1)
            
        dfs(sr,sc)
        return image