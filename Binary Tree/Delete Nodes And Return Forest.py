from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:

        parent = defaultdict()
        child = defaultdict(list)
        parent[root] = [-1, None]

        def traverse(root, p, left):
            if not root:
                return
            if p != -1:
                parent[root] = [p, left]
                child[p].append(root)
            if root.left:
                traverse(root.left, root, 1)
            else:
                child[root].append(None)
            if root.right:
                traverse(root.right, root, 0)
            else:
                child[root].append(None)

        def delete(root, d):
            if not root:
                return
            if root.val in d:
                p, left = parent[root]
                if p == -1:
                    parent[root] = [-2, 1]
                if p != -1 and left:
                    child[p][0] = None
                elif p != -1 and not left:
                    child[p][1] = None
                l, r = child[root]
                if l:
                    parent[l][0] = -1
                if r:
                    parent[r][0] = -1
            if root.left:
                delete(root.left, d)
            if root.right:
                delete(root.right, d)
            if root.val in d and p != -1 and left:
                p.left = None
            elif root.val in d and p != -1 and not left:
                p.right = None

        traverse(root, -1, 1)
        delete(root, set(to_delete))

        ans = []
        for i in parent:
            if parent[i][0] == -1:
                ans.append(i)

        return ans
