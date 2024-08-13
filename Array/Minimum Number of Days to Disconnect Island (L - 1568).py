T.C. = O(n*m)  #m = no of rows, n = no of cols
S.C. = O(n*m)
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def DFS(grid, i, j, visited, n, m):
            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or grid[i][j] == 0:
                return
            visited[i][j] = True
            for dir in directions:
                r = i + dir[0]
                c = j + dir[1]
                DFS(grid, r, c, visited, n, m)
        def noOfIslands(grid, n, m):
            visited = [[False for _ in range(m)] for _ in range(n)]
            count = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1 and not visited[i][j]:
                        DFS(grid, i, j, visited, n, m)
                        count += 1
            return count
        n = len(grid)
        m = len(grid[0])
        count = noOfIslands(grid, n, m)
        if count == 0  or count > 1:
            return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    count = noOfIslands(grid, n, m)
                    if count == 0 or count > 1:
                        return 1
                    grid[i][j] = 1
        return 2
