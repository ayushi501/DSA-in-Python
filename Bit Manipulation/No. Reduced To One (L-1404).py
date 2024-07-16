class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        i = n-1
        op = 0
        carry = 0
        while i:
            if (int(s[i]) + carry) % 2 == 0:
                op += 1
            else:
                op += 2
                carry = 1
            i -= 1
        return op + carry
