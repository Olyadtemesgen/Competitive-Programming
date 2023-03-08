# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = defaultdict(list)

        def traverse(root, row, col):
            nonlocal result

            if not root:
                return

            result[col].append([row, root.val])

            traverse(root.left, row + 1, col - 1)
            traverse(root.right, row + 1, col + 1)

        traverse(root, 0, 0)
        
        for dxx in result:
            result[dxx].sort()
        
        # print(result)
        rest = [[] for x in range(len(result))]
        aa = 0
        
        for x in result:
            rest[aa].append(x)
            
            for arr in result[x]:
                rest[aa].append(arr[1])
            
            aa += 1
        rest.sort()
        answer = []
        for x in rest:
            answer.append(x[1:])
        
        return answer
