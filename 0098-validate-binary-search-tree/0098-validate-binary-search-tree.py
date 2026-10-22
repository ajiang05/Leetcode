# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        We need to have a minimum when we go left and we need to have max when we go right

        Like a range for max and min
        """
        def helper(root,maxi,mini):
            if not root:
                return True
            if root.val>=maxi or root.val<=mini:
                return False
        
            return helper(root.left,root.val,mini) and helper(root.right,maxi,root.val)
    
        return helper(root,float('inf'),float('-inf'))
        