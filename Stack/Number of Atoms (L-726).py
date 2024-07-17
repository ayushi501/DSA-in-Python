from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0
        st = [defaultdict(int)]
        while i < n:
            if formula[i] == '(':
                st.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                mp = st[-1]
                st.pop()
                i += 1
                multiplier = ''
                while i < n and formula[i].isdigit():
                    multiplier += formula[i]
                    i += 1
                for k, v in mp.items():
                    v *= int(multiplier or '1')
                    st[-1][k] += v
            else:
                s = formula[i]
                i += 1
                while i < n and formula[i].isalpha() and formula[i].islower():
                    s += formula[i]
                    i += 1
                c = ''
                while i < n and formula[i].isdigit():
                    c += formula[i]
                    i += 1
                st[-1][s] += int(c or 1)

        mp = st[-1]
        l = sorted(mp.items())
        result = ''
        for i in l:
            result += i[0]
            if i[1] > 1:
                result += str(i[1])

        return result
