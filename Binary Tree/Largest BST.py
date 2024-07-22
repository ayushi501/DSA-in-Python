class Solution:
    def largestBst(self, root):
        # Your code here
        def solve(root):
            if not root:
                return (float('inf'), float('-inf'), 0)
            l = solve(root.left)
            r = solve(root.right)
            if l[1] < root.data and r[0] > root.data:
                return (min(l[0], root.data), max(r[1], root.data), l[2] + r[2] + 1)
            return (float('-inf'), float('inf'), max(l[2], r[2]))
        return solve(root)[2]
