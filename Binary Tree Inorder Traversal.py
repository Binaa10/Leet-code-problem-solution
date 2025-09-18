class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        current = root
        
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                # Find the inorder predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    # Create a temporary link
                    predecessor.right = current
                    current = current.left
                else:
                    # Remove the temporary link
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
        
        return result
