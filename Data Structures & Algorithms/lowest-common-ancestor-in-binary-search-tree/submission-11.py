# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #op.val1: q.val<node and p.val<node -> go left
        #op.val2 q.val>node and p.val>node->go right
        #op.val3 q.val>node p.val<node -> return node
        #op.val4 q.val==node or p.val==node-> return node
        cur=root
        if (q.val>cur.val and p.val<cur.val ) or(q.val<cur.val and p.val>cur.val) or (q.val==cur.val or p.val==cur.val)  :
            return cur
        elif not cur.right and not cur.left:
            return cur
        elif cur.left and cur.val>p.val and cur.val>q.val:
            cur=root.left
            return self.lowestCommonAncestor(cur,p,q)
        else:
            cur=root.right
            return self.lowestCommonAncestor(cur,p,q)

        
        