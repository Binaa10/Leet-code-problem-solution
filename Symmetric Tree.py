class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        if not root:
            return True
        return isMirror(root.left, root.right)
