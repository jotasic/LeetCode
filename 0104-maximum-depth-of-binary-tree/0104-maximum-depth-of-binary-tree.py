# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.cal_depth(0, root)
    
    
    def cal_depth(self, bf_depth: int,  cur_leaf: Optional[TreeNode]) -> int:
        if not cur_leaf:
            return bf_depth
        
        cur_depth = bf_depth + 1
        depths = self.cal_depth(cur_depth, cur_leaf.left), self.cal_depth(cur_depth, cur_leaf.right)
        return max(depths)