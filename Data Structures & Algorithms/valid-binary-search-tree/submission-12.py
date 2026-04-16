# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # פונקציית עזר שמקבלת את הגבולות (מינ' ומקס')
        def validate(node, low, high):
            # עץ ריק הוא תמיד BST חוקי
            if not node:
                return True
            
            # אם הערך הנוכחי חורג מהגבולות - זה לא BST
            if not (low < node.val < high):
                return False
            
            # יורדים שמאלה: המקסימום החדש הוא הערך של הצומת הנוכחי
            # יורדים ימינה: המינימום החדש הוא הערך של הצומת הנוכחי
            return validate(node.left, low, node.val) and \
                   validate(node.right, node.val, high)

        # מתחילים עם השורש וטווח של אינסוף
        return validate(root, float('-inf'), float('inf'))