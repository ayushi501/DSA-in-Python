class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse = True)
        verticalCut.sort(reverse = True)
        i, j = 0, 0
        n = len(horizontalCut)
        m = len(verticalCut)
        cost = 0
        hPieces, vPieces = 1, 1
        while i < n and j < m:
            if horizontalCut[i] >= verticalCut[j]:
                cost += horizontalCut[i] * vPieces
                hPieces += 1
                i += 1
            elif horizontalCut[i] < verticalCut[j]:
                cost += verticalCut[j] * hPieces
                vPieces += 1
                j += 1
        while i < n:
            cost += horizontalCut[i] * vPieces
            i += 1
        while j < m:
            cost += verticalCut[j] * hPieces
            j += 1
        return cost
        
