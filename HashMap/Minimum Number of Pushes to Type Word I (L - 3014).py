T.C. = O(nlogn)
S.C. = O(n)
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        l = list(sorted(c.items(), key = lambda x : x[1])) #O(nlogn)
        i = len(l) - 1
        ans = 0
        while i >= 0:                                      #O(n)
            ans += ((i//8+1) * l[i][1])
            i -= 1
        return ans
