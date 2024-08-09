T.C. = O(rows*cols)
S.C. = O(1)

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magicSquare(grid, r, c):
            l = [-1 for _ in range(9)]           #O(1)
            for i in range(3):
                for j in range(3):
                    if grid[r+i][c+j] < 1 or grid[r+i][c+j] > 9 or l[grid[r+i][c+j] - 1] != -1:
                        return False
                    l[grid[r+i][c+j] - 1] = 1
            s = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            for i in range(3):
                if grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2] != s:
                    return False
                if grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i] != s:
                    return False
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False
            return True

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows-2):                #O(rows*cols)
            for j in range(cols-2):
                if magicSquare(grid, i, j):
                    count += 1
        return count
