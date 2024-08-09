T.C. = O(n*n)
S.C. = O(n*m)

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0 for _ in range(n)] for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col = 0, -1
        spiral = n
        dir = 0
        val = 1
        while val <= n*n:
            if dir == 1 or dir == 3:
                spiral -= 1
            for i in range(spiral):
                row += directions[dir][0]
                col += directions[dir][1]
                m[row][col] = val
                val += 1
            dir = (dir + 1) % 4
        return m
