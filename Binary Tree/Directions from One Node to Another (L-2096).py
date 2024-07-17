class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach -1


class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        def findPath(r, t, s):
            if not r:
                return None
            if r.val == t:
                return ''.join(s)
            if r.left:
                s.append('L')
                res = findPath(r.left, t, s)
                if res:
                    return res
                s.pop()
            if r.right:
                s.append('R')
                res = findPath(r.right, t, s)
                if res:
                    return res
                s.pop()
            return None

        def solve(root, p, q):
            if not root:
                return None
            if root.val == p or root.val == q:
                return root
            a = solve(root.left, p, q)
            b = solve(root.right, p, q)
            if not a:
                return b
            elif not b:
                return a
            return root

        lca = solve(root, startValue, destValue)

        s = findPath(lca, startValue, [])
        t = findPath(lca, destValue, [])

        res = ''
        res += 'U' * len(s) if s else ''
        res += t if t else ''
        return res

# Approach -2


class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        def findPath(root, target, s):
            if not root:
                return None
            if root.val == target:
                return ''.join(s)
            if root.left:
                s.append('L')
                res = findPath(root.left, target, s)
                if res:
                    return res
                s.pop()
            if root.right:
                s.append('R')
                res = findPath(root.right, target, s)
                if res:
                    return res
                s.pop()
            return None

        rootToSrc = findPath(root, startValue, [])
        rootToDest = findPath(root, destValue, [])

        i = 0
        while i < len(rootToSrc) and i < len(rootToDest) and rootToSrc[i] == rootToDest[i]:
            i += 1

        res = ''
        res += 'U' * (len(rootToSrc)-i)
        res += rootToDest[i:]
        return res
