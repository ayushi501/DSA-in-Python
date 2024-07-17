# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def solve(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
            a = solve(root.left, p, q)
            b = solve(root.right, p, q)
            print(a, b)
            if not a:
                return b
            elif not b:
                return a
            return root

        return solve(root, p, q)
