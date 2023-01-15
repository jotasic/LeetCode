# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = list()

        if not root:
            return visited
        
        elif root.left:
            visited = self.inorderTraversal(root.left)
        
        visited.append(root.val)

        if root.right:
            visited += self.inorderTraversal(root.right)

        return visited