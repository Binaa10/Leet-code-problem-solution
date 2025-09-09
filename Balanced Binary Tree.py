# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return 0, True  # height, isBalanced
            
            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)
            
            # Current node is balanced if both subtrees are balanced
            # and the height difference is at most 1
            balanced = (
                left_balanced and 
                right_balanced and 
                abs(left_height - right_height) <= 1
            )
            
            # Height of current node = 1 + max subtree height
            return 1 + max(left_height, right_height), balanced
        
        # We only care about the balanced boolean
        return dfs(root)[1]
