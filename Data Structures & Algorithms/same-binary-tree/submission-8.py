# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q:
            if p:
                return False
            return True
        if not p:
            if q:
                return False
            return True
        if q.val!=p.val:
            return False
        if q.val==p.val==None:
            return True
        return self.isSameTree(p.left,q.left) and  self.isSameTree(p.right,q.right)
        