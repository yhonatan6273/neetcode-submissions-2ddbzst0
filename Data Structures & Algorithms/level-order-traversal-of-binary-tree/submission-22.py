from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        res=[]
        q.append(root)
        if not root:
            return res
        
        while q:
            cur_res=[]
            lvl_len=len(q)
            while lvl_len>0:
                cur=q.popleft()
                cur_res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                lvl_len-=1
            res.append(cur_res)
        return res


        