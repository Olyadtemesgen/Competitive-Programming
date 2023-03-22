# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        val = None
        prevv = None
        
        def real_finder(prev, root):
            
            nonlocal val
            nonlocal prevv

            if not root:
                return
            
            if root.val == key:
                prevv = prev
                val = root
                return
            if root.val > key:
                real_finder(root, root.left)
            else:
                real_finder(root, root.right)
        
        real_finder(None, root)
        
        
        if not val:
            return root
        print(val.val)

        if not val.left and not val.right:
            if prevv:
                if prevv.left == val:
                    prevv.left = None
                else:
                    prevv.right = None
            

                return root
        
        if prevv and val:
            
            if not val.right:
                
                if prevv.right == val:
                    prevv.right = val.left
                
                else:
                    prevv.left = val.left
                
                return root
            elif not val.left:
                if prevv.right == val:
                    prevv.right = val.right

                else:
                    prevv.left = val.right
                
                return root
            prevs = val
            roots = val.right
            
            def find_replacer(prev, root):

                nonlocal prevs
                nonlocal roots
                
                if not root.left:
                    prevs = prev
                    roots = root
                    return
                
                find_replacer(root, root.left)
            
            find_replacer(prevs, roots)
            
            print(prevs.val)
            if prevs == val:

                saved = val.left
                print(prevv.val)
                if prevv:
                    if prevv.left == prevs:
                       prevv.left = roots
                    
                    else:
                        prevv.right = roots

                roots.left = saved
                
                return root
            
            else:
                prevs.left = roots.right
                val.val = roots.val

            return root

        if not prevv:
            
            if not val:
                return None

            if not val.right:
                return root.left
            
            elif not val.left:
                return root.right
        
            another = val
            prevs = None

            def againfinder(prev, root):
                
                nonlocal another
                nonlocal prevs
                
                if not root.left:
                    if not prev:
                        saved = another.left
                        another = another.right
                        another.left = saved
                    
                    else:
                        prev.left = root.right
                        another.val = root.val
                    return
                
                againfinder(root, root.left)
            
            againfinder(None, another.right)

            return another