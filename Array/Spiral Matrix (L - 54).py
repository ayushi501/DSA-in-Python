T.C. = O(n)
S.C. = O(n) #for answer

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir = 0
        spiralC = n
        spiralR = m-1
        size = 0
        row, col = 0, -1
        while size < m*n:
            spiral = 0
            if dir == 0 or dir == 2:
                spiral = spiralC
                spiralC -= 1
            else:
                spiral = spiralR 
                spiralR -= 1
            for i in range(spiral):
                row += directions[dir][0]
                col += directions[dir][1]
                ans.append(matrix[row][col])
                size += 1
            dir = (dir + 1) % 4
        return ans
