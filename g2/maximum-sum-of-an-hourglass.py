class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        result = 0
        for x in range(len(grid)):
            for y in range(1,len(grid[0])):
                grid[x][y] += grid[x][y - 1]
        print(grid)
        for x in range(2, len(grid)):
            result = max(result, grid[x][2] + grid[x - 1][1] - grid[x - 1][0] + grid[x - 2][2])
        for ab in range(2, len(grid)):
            for bc in range(3, len(grid[0])):
                result = max(result, grid[ab][bc] - grid[ab][bc - 3] - grid[ab - 2][bc - 3] + grid[ab - 1][bc - 1] + grid[ab - 2][bc] - grid[ab - 1][bc - 2] )
        return result
# class Solution:
#     def maxSum(self, grid: List[List[int]]) -> int:
#         colen = len(grid[0]) + 1
#         rowlen = len(grid)
#         for x in range(rowlen):
#             grid[x] = [0] + grid[x]
#         for row in range(rowlen):
#             for col in range(1, colen):
#                 grid[row][col] += grid[row][col - 1]
#         print(grid)
#         res = 0
#         if not rowlen - 3:
#             while colen - 3:
#                 colen -= 1
#                 res = max(res, grid[0][colen] - grid[0][colen - 3] + grid[2][colen] - grid[2][colen - 3] + grid[1][colen - 1] - grid[1][colen - 2])
#                 print(res)
#             return res
#         for row in range(rowlen - 2):
#             for col in range(3, colen):
#                 res = max(res, grid[row][col] - grid[row][col - 3] + grid[row + 2][col] - grid[row + 2][col - 3] + grid[row + 1][col - 1] - grid[row + 1][col - 2])
#         return res
