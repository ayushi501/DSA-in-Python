T.C. = O(n)
S.C. = O(1)
class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        i = 0
        while i < len(word):    #O(n)
            ans += i//8 + 1
            i += 1
        return ans
