# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i,j=0,0
        def dfs(value):
            nonlocal i,j
            if i>=len(preorder):
                return None
            if inorder[j]==value:
                j+=1
                return None

            root=TreeNode(preorder[i])
            i+=1
            root.left=dfs(root.val)
            root.right=dfs(value)
            return root
        return dfs(float("inf"))

     
      