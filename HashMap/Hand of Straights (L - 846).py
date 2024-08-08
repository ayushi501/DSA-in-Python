T.C. = O(nlogn)
S.C. = O(n)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        l = list(sorted(c.items()))                    #O(nlogn)
        i = 0
        while i < len(l):                              #O(n*groupSize)
            k = l[i][0]
            j = 0
            while i+j < len(l) and j < groupSize:      
                if l[i+j][0] != (k+j) or l[i+j][1] == 0:
                    return False
                a = l[i+j][0]
                b = l[i+j][1] - 1
                l[i+j] = (a, b)
                j += 1
            if j != groupSize:
                return False
            while i < len(l) and l[i][1] == 0:
                i += 1
        return True
