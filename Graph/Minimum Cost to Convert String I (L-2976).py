class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = [[float('inf') for i in range(26)] for i in range(26)]
        for i in range(len(original)):
            o = ord(original[i]) - ord('a')
            c = ord(changed[i]) - ord('a')
            adj[o][c] = min(adj[o][c], cost[i])
        for i in range(26):
            adj[i][i] = 0

        def floydWarshell():
            for k in range(26):
                for i in range(26):
                    for j in range(26):
                        adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        
        floydWarshell()
        cost = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            else:
                s = ord(source[i]) - ord('a')
                t = ord(target[i]) - ord('a')
                if adj[s][t] == float('inf'):
                    return -1
                cost += adj[s][t]
        return cost
