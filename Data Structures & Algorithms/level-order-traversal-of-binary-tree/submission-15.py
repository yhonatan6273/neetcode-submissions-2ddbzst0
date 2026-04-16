from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        
        lvl=deque([root])
       
        while lvl:
            cur_lvl=[]
            lenlvl=len(lvl)
            for _ in range(lenlvl):

                cur_node=lvl.popleft()
                cur_lvl.append(cur_node.val)
                if cur_node.left:
                    lvl.append(cur_node.left)
                if cur_node.right:
                    lvl.append(cur_node.right)
            res.append(cur_lvl)
       
        return res


        