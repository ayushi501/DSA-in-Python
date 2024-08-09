T.C. = O(max(m, n)*max(m, n)) > O(m*n)   # m = rows, n = cols
S.C. = O(m*n)

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        spiral = 0
        dir = 0
        row, col = rStart, cStart
        ans = [(row, col)]
        size = 1
        while size < (rows * cols):
            if dir == 0 or dir == 2:
                spiral += 1
            for i in range(spiral):
                row += directions[dir][0]
                col += directions[dir][1]
                if row >= 0 and row < rows and col >= 0 and col < cols:
                    ans.append((row, col))
                    size += 1
            dir = (dir + 1) % 4
        return ans 

