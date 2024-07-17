class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        m = {}
        parent = set()
        u = TreeNode(-1)
        for i in descriptions:
            p = i[0]
            c = i[1]
            d = i[2]
            if p not in m:
                n = TreeNode(p)
                m[p] = n
                parent.add(p)
            else:
                n = m[p]
            if c not in m:
                a = TreeNode(c)
                m[c] = a
            else:
                a = m[c]
                if c in parent:
                    parent.remove(c)
            if d == 1:
                n.left = a
            else:
                n.right = a

        if len(parent) != 1:
            ans = list(parent)
            return m[ans[-1]]
        for i in parent:
            return m[i]
